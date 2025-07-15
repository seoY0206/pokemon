# Github  Action
# 1. py
# 2. 어떤 os에서 동작? ubuntu(리눅스)
# 3. 크롤링 - selenium
# - 브라우저를 켜지 않아도 할 수 있는지
# - linux 크롬 드라이버

from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless") # 창 없음
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

url_pokemon = "https://pokemonkorea.co.kr/pokedex"
driver = wb.Chrome(options=options)
driver.maximize_window()
driver.get(url_pokemon)
img = driver.find_element(By.CSS_SELECTOR, "img.img-fluid")
img.click()
time.sleep(1)
h3 = driver.find_element(By.TAG_NAME, "h3")
name = h3.text.split("\n")[1]

driver.close()

import csv
import os
pokemon_exist = os.path.exists("pokemon.csv")
header = ["no", "name"]

with open("pokemon.csv", "a", newline = "") as file:
    writer = csv.writer(file)

    if not pokemon_exist:
        writer.writerow(header)

    writer.writerow(["0001", name])
    print("포켓몬 저장 완료")
