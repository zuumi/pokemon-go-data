import requests
from bs4 import BeautifulSoup
import json

# 取得したいデータの掲載先
url = "https://pokemongo.gamewith.jp/article/show/35502"

# Responseオブジェクト生成
response = requests.get(url)

# 文字化け防止
response.encoding = response.apparent_encoding

# BeautifulSoupオブジェクト生成
soup = BeautifulSoup(response.text, "html.parser")

# テーブルを取得
table = soup.find("table", class_='sorttable')
pokemon_data = {}

# テーブル内のデータを取得する
for row in table.find_all('tr'):
		div = row.find('div')
		if div:
			pokemon_id = div['id']
			pokemon_name = div.text
			pokemon_url = div.find('a')['href']
			pokemon_data[pokemon_id] = {'name': pokemon_name, 'url': pokemon_url}

data = {'pokemon_data': pokemon_data}

with open('pokemon_data.json', 'w', encoding='utf-8') as f:
	json.dump(data, f, ensure_ascii=False, indent=4)

print("JSONファイルに出力しました。")
		
