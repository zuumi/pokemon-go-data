import requests
from bs4 import BeautifulSoup
import json

STAGING_JSON = 'pokemon_data_test.json'
PRODUCTION_JSON = 'pokemon_data.json'
SAVE_JSON = STAGING_JSON

with open(SAVE_JSON, 'r', encoding='utf-8') as f:
    data = json.load(f)

def getWaza(rows,pokemon_data):
    pokemon_data = []
    for row in rows:
        data_row = list()
        columns = row.find_all('td')
        for column in columns:
            a_tag = column.find('a')
            if a_tag:
                data_row.append(a_tag.text)
        pokemon_data.append(data_row)
    return pokemon_data

# 各ポケモンのURLからデータを取得して追加
for pokemon_id, pokemon_info in data[SAVE_JSON].items():
    try:
        url = pokemon_info['url']
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        tables = soup.find('div', class_='pgo_hyouka_waza').find_all('table')
        if tables is None:
            continue
        rowsA = tables[0].find('table').find_all('tr')[1:]
        rowsB = tables[1].find('table').find_all('tr')[1:]
        pokemon_info['waza'] = getWaza(rowsA)
        pokemon_info['waza'] = getWaza(rowsB)

    except AttributeError:
        pokemon_info['waza'] = []
        continue


# 更新されたデータをpokemon_data.jsonに保存
with open(SAVE_JSON, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("JSONファイルに出力しました。")
