import csv
import time
import re
import unicodedata
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def normalize_name(name):
    nfkd = unicodedata.normalize('NFKD', name)
    return ''.join(c for c in nfkd if not unicodedata.combining(c)).lower().strip()

input_csv = r"C:\Users\Admin\OneDrive\Desktop\BTL PYTHON\BÀI 1\results.csv"
with open(input_csv, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    data = list(reader)

Name = { normalize_name(r["Name"]): r for r in data }

# --- Bước 1 : Khởi tạo Selenium ---
driver = webdriver.Chrome()
driver.get("https://www.footballtransfers.com/en/values/players/most-valuable-players/playing-in-uk-premier-league")

# --- Bước 2: Duyệt qua các trang, parse bằng BeautifulSoup ---
for page in range(1, 23):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    table = soup.find("tbody", id="player-table-body")
    for tr in table.find_all("tr"):
        a = tr.find("a")
        tag = tr.find("span", class_="player-tag")
        if not a or not tag:
            continue
        name = a.get_text(strip=True)
        m = re.search(r"([\d\.]+)", tag.get_text())
        if not m: continue
        val = m.group(1)
        norm = normalize_name(name)
        if norm in Name:
            Name[norm]["ETV(€M)"] = val
    #next page
    if page < 22:
        btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "pagination_next_button"))
        )
        btn.click()
        time.sleep(2)

driver.quit()

# --- Bước 3: Xuất data.csv (lọc minutes > 900 và có ETV) ---
output_csv = "data.csv"
fields = list(data[0].keys())
if "ETV(€M)" not in fields:
    fields.append("ETV(€M)")

with open(output_csv, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=fields, restval="N/a")
    writer.writeheader()
    for r in data:
        etv = r.get("ETV(€M)", "").strip()
        mins = r.get("Minutes", "").replace(",", "").strip()
        if etv and mins.isdigit() and int(mins) > 900:
            writer.writerow(r)

