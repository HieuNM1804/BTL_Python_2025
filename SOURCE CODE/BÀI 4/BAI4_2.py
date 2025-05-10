import pandas as pd
from sklearn.model_selection import RepeatedKFold, GridSearchCV
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.inspection import permutation_importance
from sklearn.metrics import make_scorer, r2_score

# 1. Đọc file
df = pd.read_csv('data.csv', encoding='utf-8-sig', na_values=['N/a'], thousands=',')
df = df.drop(['Team','Nation','Position','Name'], axis=1, errors='ignore')
for c in df.select_dtypes(include='object').columns:
    df[c] = pd.to_numeric(df[c].str.replace(',', ''), errors='coerce')
df.fillna(df.mean(), inplace=True)

# 2. X : data, y : target
target = df.columns[-1]
X = df.drop(columns=[target])
y = df[target]


# 3. Tìm top10 các feature quan trọng
base = HistGradientBoostingRegressor(random_state=42)
base.fit(X, y)
imp = permutation_importance(base, X, y, scoring='r2', n_repeats=15, random_state=42, n_jobs=-1)
imp_ser = pd.Series(imp.importances_mean, index=X.columns).sort_values(ascending=False)
top10 = imp_ser.iloc[:10].index.tolist()


# 4. Dữ liệu tham số
param_grid = {
    'max_iter': [100, 150, 200],
    'learning_rate': [0.03, 0.05],
    'max_depth': [2, 3, 4],
    'min_samples_leaf': [10, 15, 20],
    'max_bins': [128, 256]
}

hgb = HistGradientBoostingRegressor(random_state=42)

# 5. GridSearchCV 
rkf = RepeatedKFold(n_splits=5, n_repeats=3, random_state=42)
search = GridSearchCV(
    estimator=hgb,
    param_grid=param_grid,
    scoring=make_scorer(r2_score),
    cv=rkf,
    n_jobs=-1,
    verbose=2
)

# 6. Fit 
search.fit(X[top10], y)

print('Best feature')
print(*top10)

# 7. Tham số tốt nhất
print("Best parameters found:")
print(search.best_params_)
print(f"Best CV R²: {search.best_score_:.4f}")

best_hgb = search.best_estimator_
best_hgb.fit(X[top10], y)
print("Final model trained on all data.")

# 9. Visualize CV results 
cv_df = pd.DataFrame(search.cv_results_)
pivot = cv_df.pivot_table(
    index='param_learning_rate',
    columns='param_max_iter',
    values='mean_test_score'
)
import matplotlib.pyplot as plt
best_params = search.best_params_
best_r2 = search.best_score_
rows = list(best_params.items()) + [('CV R²', f"{best_r2:.4f}")]
col_labels = ["Parameter", "Value"]
cell_text = [[k, str(v)] for k, v in rows]
fig, ax = plt.subplots(figsize=(6, len(rows)*0.5))
ax.axis('off')
tbl = ax.table(
    cellText=cell_text,
    colLabels=col_labels,
    cellLoc='center',
    loc='upper center'
)
tbl.auto_set_font_size(False)
tbl.set_fontsize(12)
tbl.scale(1, 1.5)
plt.title("Best Hyperparameters and CV R²", pad=20)
plt.tight_layout()
plt.show()
