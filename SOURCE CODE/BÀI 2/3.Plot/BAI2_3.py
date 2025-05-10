import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

plots_dir  = Path(__file__).parent / 'plots'
plots_dir.mkdir(exist_ok=True)
#Đọc và chuẩn hóa dữ liệu
df = pd.read_csv(r'C:\Users\Admin\OneDrive\Desktop\BTL PYTHON\BÀI 1\results.csv', encoding='utf-8-sig', thousands=',')
df.replace('N/a', np.nan, inplace=True)
attack_stats  = ['Goals', 'Assists', 'GCA']            
defense_stats = ['Tkl', 'Sh', 'Int']
plot_stats    = [s for s in (attack_stats + defense_stats) if s in df.columns]
# Ép kiểu numeric
for stat in plot_stats:
    df[stat] = pd.to_numeric(df[stat].astype(str).str.replace(',', ''), errors='coerce')
# Danh sách đội
teams = df['Team'].dropna().unique()


# Vẽ và lưu histogram
for stat in plot_stats:
    # Histogram cho toàn giải
    vals_all = df[stat].dropna()
    plt.figure(figsize=(6,4))
    plt.hist(vals_all, bins='auto', edgecolor='black') 
    plt.title(f'{stat}  All Players')
    plt.xlabel(stat)
    plt.ylabel('Count')
    plt.tight_layout()
    # Lưu file
    fname = plots_dir / f"{stat}_all.png"
    plt.savefig(fname)
    plt.close()
    # Histogram cho từng đội
    for team in teams:
        vals_team = df.loc[df['Team']==team, stat].dropna()
        if vals_team.empty:
            continue
        plt.figure(figsize=(6,4))
        plt.hist(vals_all, bins='auto', edgecolor='black')
        plt.title(f'{stat}  {team}')
        plt.xlabel(stat)
        plt.ylabel('Count')
        plt.tight_layout()
        fname = plots_dir / f"{stat}_{team.replace(' ', '_')}.png"
        plt.savefig(fname)
        plt.close()
