import requests
from bs4 import BeautifulSoup
import json

STAGING_JSON = 'pokemon_data_test.json'
PRODUCTION_JSON = 'pokemon_data.json'
SAVE_JSON = STAGING_JSON

def getWaza(rows):
    for row in rows:
        pokemon_data = list()
        columns = row.find_all('td')
        for column in columns:
            a_tag = column.find('a')
            if a_tag:
                pokemon_data.append(a_tag.text)

    return pokemon_data

def main():
    with open(SAVE_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # 各ポケモンのURLからデータを取得して追加
    for pokemon_id, pokemon_info in data[SAVE_JSON].items():
        try:
            url = pokemon_info['url']
            response = requests.get(url)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            tables = soup.find_all('div', class_='pgo_hyouka_waza')
            waza = list()
            if tables is None:
                continue
            for i, table in enumerate(tables):
                if i == 2 or i==3:
                    continue
                
                waza.append(getWaza(table.find_all('table')))
                
                pokemon_info['waza'] = waza
                print('.')

            print('.')


        except AttributeError:
            pokemon_info['waza'] = []
            continue

    # 更新されたデータをpokemon_data.jsonに保存
    with open(SAVE_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("JSONファイルに出力しました。")

if __name__ == "__main__":
    main()
