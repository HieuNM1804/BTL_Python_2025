import pandas as pd
import numpy as np
from pathlib import Path

#  Đọc và chuẩn hóa dữ liệu
df = pd.read_csv( r'C:\Users\Admin\OneDrive\Desktop\BTL PYTHON\BÀI 1\results.csv', encoding='utf-8-sig', thousands=',')
df.replace('N/a', np.nan, inplace=True)
#  Xác định các feature và ép kiểu numeric
exclude = ['Name', 'Nation', 'Position', 'Team']
stats   = [c for c in df.columns if c not in exclude]
for stat in stats:
    df[stat] = pd.to_numeric( df[stat].astype(str).str.replace(',', ''), errors='coerce')

# Tính mean theo team
team_means   = df.groupby('Team')[stats].mean()
best_by_mean = team_means.idxmax()
best_values  = team_means.max()

# Chuẩn bị report_df
report_df = pd.DataFrame({
    'Feature':    best_by_mean.index,
    'Top Team':   best_by_mean.values,
    'Mean Value': best_values.values.round(2)
})

# Chuẩn bị summary_df
lead_counts  = best_by_mean.value_counts().reset_index()
summary_df   = lead_counts.copy()
summary_df.columns = ['Team', 'Num Features highest score']

# Ghi ra out.csv
out_path = Path(__file__).parent / 'out.csv'
with open(out_path, 'w', encoding='utf-8-sig', newline='') as f:
    report_df.to_csv(f, index=False)
    f.write('\n')
    summary_df.to_csv(f, index=False)

