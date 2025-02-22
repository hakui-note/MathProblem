from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# 検索ワードを入力する
keyword = "東京"

# Windows用：chromedriverのパスを指定
# chrome = webdriver.Chrome("ここにパスを記載する")

# mac用
chrome = webdriver.Chrome(r"c:\Users\ハクイ\OneDrive\ドキュメント\Python Scripts\chromedriver")

# Chromeでサイトへアクセス
chrome.get('https://google.com')

time.sleep(3)

# 検索ボックスのnameをセット
search_box = chrome.find_elements(By.CLASS_NAME,"q")

# 入力した検索ワードを検索欄に出力
search_box.send_keys(keyword)

# 検索実行
search_box.send_keys(Keys.RETURN)