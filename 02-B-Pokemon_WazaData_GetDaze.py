import requests
from bs4 import BeautifulSoup
import json

STAGING_JSON = 'pokemon_data.json'
PRODUCTION_JSON = 'pokemon_data.json'
SAVE_JSON = PRODUCTION_JSON

with open(SAVE_JSON, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 各ポケモンのURLからデータを取得して追加
for pokemon_id, pokemon_info in data['pokemon_data'].items():
    try:
        url = pokemon_info['url']
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('div', class_='pgo_hyouka_waza').find('table')
        rows = table.find_all('tr')[1:]
        pokemon_data = []
        for row in rows:
            data_row = list()
            columns = row.find_all('td')
            for column in columns:
                a_tag = column.find('a')
                if a_tag:
                    pokemon_data.append(a_tag.text)
        pokemon_info['waza'] = pokemon_data
    except AttributeError:
        pokemon_info['waza'] = []
        continue


# 更新されたデータをpokemon_data.jsonに保存
with open(SAVE_JSON, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("JSONファイルに出力しました。")