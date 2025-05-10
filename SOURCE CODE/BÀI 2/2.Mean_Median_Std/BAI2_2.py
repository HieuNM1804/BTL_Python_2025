import pandas as pd
import numpy as np


df = pd.read_csv(r'C:\Users\Admin\OneDrive\Desktop\BTL PYTHON\BÀI 1\results.csv', encoding='utf-8-sig', thousands=',')
df.replace('N/a', np.nan, inplace=True)
exclude = ['Name','Nation','Position']
stats   = [c for c in df.columns if c not in exclude + ['Team']]
for stat in stats:
    df[stat] = pd.to_numeric(df[stat].astype(str).str.replace(',', ''), errors='coerce')
scopes = ['All'] + df['Team'].dropna().unique().tolist()
cols = ['Teams']
for stat in stats:
    cols += [f'Median of {stat}', f'Mean of {stat}', f'Std of {stat}']



rows = []
for scope in scopes:
    row = {'Teams': scope}
    if scope == 'All':
        subdf = df
    else:
        subdf = df[df['Team'] == scope]
    for stat in stats:
        arr = subdf[stat].dropna()
        row[f'Median of {stat}'] = arr.median()
        row[f'Mean of {stat}']   = arr.mean()
        row[f'Std of {stat}']    = arr.std()
        print(type(arr))
    rows.append(row)
res2 = pd.DataFrame(rows, columns=cols)
res2.to_csv('results2.csv', index=False, encoding='utf-8-sig')