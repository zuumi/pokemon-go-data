import json

LOAD_JSON = 'PokemonGO-waza-3.json'
SAVE_JSON = 'pokemon_data_waza_3.json'

# JSONデータをPythonのリストに変換
with open(LOAD_JSON, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 'わざ'の値を基準にソート
sorted_data = sorted(data, key=lambda x: x['わざ'])

# ソートしたデータをJSON形式に変換
sorted_json = json.dumps(sorted_data, ensure_ascii=False, indent=2)

# ソートしたデータをファイルに保存
with open(SAVE_JSON, 'w', encoding='utf-8') as f:
    f.write(sorted_json)

print(f"Sorted data has been saved to {SAVE_JSON}")
