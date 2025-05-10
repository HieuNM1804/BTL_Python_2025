PAGES = [
    #General
    {
        'url'               :       'https://fbref.com/en/comps/9/stats/Premier-League-Stats',
        'table_id'          :       'stats_standard',
        'filter'            :       'minutes',
        'stats': {
            'Position'      :       'position',
            'Age'           :       'birth_year',
            #Playing Time
            'Matches_played':       'games',
            'Starts'        :       'games_starts',
            'Minutes'       :       'minutes',
            #Performance
            'Goals'         :       'goals',
            'Assists'       :       'assists',
            'Yellow Cards'  :       'cards_yellow',
            'Red Cards'     :       'cards_red',
            #Expected
            'Expected_xG'   :       'xg',
            'Expected_xAG'  :       'xg_assist',
            #Progression
            'PrgC'          :       'progressive_carries',
            'PrgP'          :       'progressive_passes',
            'PrgR'          :       'progressive_passes_received',
            #Per 90 minutes
            'Per90_Gls'     :       'goals_per90',
            'Per90_Ast'     :       'assists_per90',
            'Per90_xG90'    :       'xg_per90',
            'Per90_xAG'     :       'xg_assist_per90',
        }
    },
    #Goalkeeping
    {
        'url'               :       'https://fbref.com/en/comps/9/keepers/Premier-League-Stats',
        'table_id'          :       'stats_keeper',
        'filter'            :       'minutes',
        'stats': {
            
            #Performance
            'GA90'          :       'gk_goals_against_per90',
            'Save%'         :       'gk_save_pct',
            'CS%'           :       'gk_clean_sheets_pct',
            #Penalty Kicks
            'PK_Save%'      :       'gk_pens_save_pct',
        }
    },
    #Shooting
    {
        'url'               :       'https://fbref.com/en/comps/9/shooting/Premier-League-Stats',
        'table_id'          :       'stats_shooting',
        'filter'            :       'minutes',
        'stats': {
            #Standard
            'SoT%'          :       'shots_on_target_pct',
            'SoT/90'        :       'shots_on_target_per90',
            'G/sh'          :       'goals_per_shot',
            'Dist'          :       'average_shot_distance',
        }
    },
    #Passing
    {
        'url'               :       'https://fbref.com/en/comps/9/passing/Premier-League-Stats',
        'table_id'          :       'stats_passing',
        'filter'            :       'minutes',
        'stats': {
            #Total
            'Cmp'           :       'passes_completed',
            'Total_Cmp%'    :       'passes_pct',
            'TotDist'       :       'passes_total_distance',
            #Short
            'Short_Cmp%'    :       'passes_pct_short',
            #Medium
            'Medium_Cmp%'   :       'passes_pct_medium',
            #Long
            'Long_Cmp%'     :       'passes_pct_long',
            #Expected
            'KP'            :       'assisted_shots',
            'Expected_1/3'  :       'passes_into_final_third',
            'PPA'           :       'passes_into_penalty_area',
            'CrsPA'         :       'crosses_into_penalty_area',
            'Expected_PrgP' :       'progressive_passes',
        }
    },
    #Goal and Shot Creation
    {
        'url'               :       'https://fbref.com/en/comps/9/gca/Premier-League-Stats',
        'table_id'          :       'stats_gca',
        'filter'            :       'minutes',
        'stats': {
            #SCA
            'SCA'           :       'sca',
            'SCA90'         :       'sca_per90',
            #GCA
            'GCA'           :       'gca',
            'GCA90'         :       'gca_per90',
        }
    },
    #Defensive Actions
    {
        'url'               :       'https://fbref.com/en/comps/9/defense/Premier-League-Stats',
        'table_id'          :       'stats_defense',
        'filter'            :       'minutes',
        'stats': {
            #Tackles
            'Tkl'           :       'tackles',
            'TklW'          :       'tackles_won',
            #Challenges
            'Challenges_Att':       'challenges',
            'Challenges_Lost':      'challenges_lost',
            #Blocks
            'Blocks'        :       'blocks',
            'Sh'            :       'blocked_shots',
            'Pass'          :       'blocked_passes',
            'Int'           :       'interceptions',
        }
    },
    #Possession
    {
        'url'               :       'https://fbref.com/en/comps/9/possession/Premier-League-Stats',
        'table_id'          :       'stats_possession',
        'filter'            :       'minutes',
        'stats': {
            #Touches
            'Touches'       :       'touches',
            'Def Pen'       :       'touches_def_pen_area',
            'Def 3rd'       :       'touches_def_3rd',
            'Mid 3rd'       :       'touches_mid_3rd',
            'Att 3rd'       :       'touches_att_3rd',
            'Att Pen'       :       'touches_att_pen_area',
            #Take-Ons
            'Take-Ons_Att'  :       'take_ons',
            'Succ%'         :       'take_ons_won_pct',
            'Tkld%'         :       'take_ons_tackled_pct',
            #Carries    
            'Carries'       :       'carries',
            'ProDist'       :       'carries_progressive_distance',
            'Carries_PrgC':         'progressive_carries',
            '1/3'           :       'carries_into_final_third',
            'CPA'           :       'carries_into_penalty_area',
            'Mis'           :       'miscontrols',
            'Dis'           :       'dispossessed',
            #Receiving
            'Rec'           :       'passes_received',
            'Receiving_PrgR':       'progressive_passes_received',
        }
    },
    #Miscellaneous Stats
    {
        'url'               :       'https://fbref.com/en/comps/9/misc/Premier-League-Stats',
        'table_id'          :       'stats_misc',
        'filter'            :       'minutes',
        'stats': {
            #Performance
            'Fls'           :       'fouls',
            'Fld'           :       'fouled',
            'Off'           :       'offsides',
            'Crs'           :       'crosses',
            'Recov'         :       'ball_recoveries',
            #Aerial Duels
            'Won'           :       'aerials_won',
            'Lost'          :       'aerials_lost',
            'Won%'          :       'aerials_won_pct',
        }
    },
]

def get_data(row, data_stat):
    cell = row.find('td', {'data-stat': data_stat})
    return cell.get_text(strip=True) if cell and cell.get_text(strip=True) else 'N/a'

import time
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome()
# Lấy Page[0] để xử lý các thông tin chung trước
std = PAGES[0]
driver.get(std['url'])
time.sleep(4)
soup0 = BeautifulSoup(driver.page_source, 'html.parser')
table0 = soup0.find('table', {'id': std['table_id']}).find('tbody')

players = {}            # key = (Name, Team) → dict chứa tất cả stats
satisfy_player = set()   # tập (Name, Team) đã chơi > 90'


for row in table0.find_all('tr'):
    # loại bỏ dòng tiêu đề
    if 'thread' in row.get('class', []):
        continue
    #check thời gian thi đấu
    mn = get_data(row, std['filter'])
    if mn == 'N/a' or int(mn.replace(',', '')) <= 90:
        continue
    name = get_data(row, 'player')
    team = get_data(row, 'team')
    key  = (name, team)
    satisfy_player.add(key)
    # Quốc tịch
    nat_cell = row.find('td', {'data-stat': 'nationality'})
    span = nat_cell.find('span') if nat_cell else None
    nation = span.contents[-1].strip() if span and span.contents else 'N/a'
    # Khởi tạo dict với tất cả cột của stats_standard
    players[key] = {'Name': name, 'Team': team, 'Nation': nation}
    for col, ds in std['stats'].items():
        val = get_data(row, ds)
        # Nếu col là Age mà file trả về birth_year, thì tính ngược
        if col == 'Age' and val.isdigit():
            players[key][col] = str(2025 - int(val))
        else:
            players[key][col] = val


#. VÒNG 2: Duyệt tiếp các page còn lại, chỉ cập nhật nếu key trong satisfy_player ===
for page in PAGES[1:]:
    driver.get(page['url'])
    time.sleep(4)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    body = soup.find('table', {'id': page['table_id']}).find('tbody')

    for row in body.find_all('tr'):
        if 'thread' in row.get('class', []):
            continue

        name = get_data(row, 'player')
        team = get_data(row, 'team')
        key  = (name, team)
        #kiểm tra key có nằm trong set hay không
        if key not in satisfy_player:
            continue

        # Cập nhật thêm các cột stats của page này
        for col, ds in page['stats'].items():
            players[key][col] = get_data(row, ds)

driver.quit()

# === Xuất file CSV với BOM UTF-8 và sắp theo Name → Team ===
fieldnames = ['Name', 'Team', 'Nation'] + [
    c for p in PAGES for c in p['stats'].keys()
]


import csv
with open('results.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, restval='N/a')
    writer.writeheader()
    for pl in sorted(players.values(), key=lambda x: (x['Name'].lower(), x['Team'].lower())):
        writer.writerow(pl)
