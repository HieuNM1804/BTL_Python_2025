import pandas as pd
import numpy as np


df = pd.read_csv(r'C:\Users\Admin\OneDrive\Desktop\BTL PYTHON\BÀI 1\results.csv', encoding='utf-8-sig', thousands=',')
df.replace('N/a', np.nan, inplace=True)
stats = [c for c in df.columns if c not in ['Name', 'Team', 'Nation', 'Position']]

for stat in stats:
    df[stat] = pd.to_numeric(df[stat].astype(str).str.replace(',', ''),  errors='coerce')

with open('top_3.txt', 'w', encoding='utf-8') as f:
    for stat in stats:
        sub = df[['Name', 'Team', 'Nation', 'Position', stat]].dropna(subset=[stat])
        f.write(f'--- {stat} ---\n')
        if sub.empty:
            f.write('Không có dữ liệu\n\n')
            continue
        bottom3 = sub.nsmallest(3, stat)
        top3    = sub.nlargest(3, stat)
        f.write('Top 3 lowest:\n')
        for _, r in bottom3.iterrows():
            f.write(f"  {r['Name']} trong đội {r['Team']} : {r[stat]}\n")
        f.write('Top 3 highest:\n')
        for _, r in top3.iterrows():
            f.write(f"  {r['Name']} trong đội {r['Team']} : {r[stat]}\n")
        f.write('\n')


        