import csv
import requests
from bs4 import BeautifulSoup


# 取得したいデータの掲載先
url = "https://wiki.xn--rckteqa2e.com/wiki/Pok%C3%A9mon_GO%E3%81%AB%E7%99%BB%E5%A0%B4%E3%81%99%E3%82%8B%E6%8A%80%E4%B8%80%E8%A6%A7"

# Responseオブジェクト生成
response = requests.get(url)

# 文字化け防止
response.encoding = response.apparent_encoding

# BeautifulSoupオブジェクト生成
soup = BeautifulSoup(response.text, "html.parser")

# テーブルを取得
tables = soup.find_all("table", class_='sortable wikitable')

# テーブル内のデータを取得する
for i, table in enumerate(tables):
	data = []
	if i == 1 or i == 3:
		for row in table.find_all('tr'):
			row_data = []
			for cell in row.find_all(['th', 'td']):
				row_data.append(cell.get_text(strip=True))
			data.append(row_data)	

	# CSVファイルにデータを書き込む
		with open('PokemonGO_WazaData_'+str(i)+'.csv', 'w', newline='', encoding='utf-8') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerows(data)

print("CSVファイルに出力しました。")
		
