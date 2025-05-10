import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Đọc dữ liệu và chuẩn hóa
df = pd.read_csv( r'C:\Users\Admin\OneDrive\Desktop\BTL PYTHON\BÀI 1\results.csv', encoding='utf-8-sig', thousands=',')
df_clean = df.drop(['Name', 'Team', 'Nation', 'Position'], axis=1)
df_clean = df_clean.apply(pd.to_numeric, errors='coerce')
means = df_clean.mean(numeric_only=True)
df_clean.fillna(means, inplace=True)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_clean)


# Xác định k, sử dụng elbow (inertia) và silhouette
Ks = range(2, 11)
elbow = []
silhouettes = []

for k in Ks:
    km = KMeans(n_clusters=k, random_state=42)
    labels = km.fit_predict(X_scaled)
    elbow.append(km.inertia_)
    silhouettes.append(silhouette_score(X_scaled, labels))


# Plot elbow và silhouette
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(Ks, elbow, 'o-')
plt.title('Elbow Method')
plt.xlabel('k')
plt.ylabel('Inertia (SSE)')

plt.subplot(1, 2, 2)
plt.plot(Ks, silhouettes, 'o-')
plt.title('Silhouette Scores')
plt.xlabel('k')
plt.ylabel('Silhouette Score')

plt.tight_layout()
plt.savefig('elbow_silhouette.png', dpi=300)
plt.show()


best_k = 3
# KMeans với k = 3 and và visualize  PCA
kmeans_opt = KMeans(n_clusters = best_k, random_state=42)
labels_opt = kmeans_opt.fit_predict(X_scaled)
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X_scaled)
plt.figure()
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels_opt, cmap='tab10')
plt.title(f'KMeans Clusters (k={best_k})')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.savefig('cluster_pca.png', dpi=300)
plt.show()