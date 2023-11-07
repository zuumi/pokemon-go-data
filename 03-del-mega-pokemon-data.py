import json

# JSONデータをロード
with open('pokemon_data.json', 'r') as f:
    data = json.load(f)

# 「メガ」で始まる名前のブロックを削除
data = {k: v for k, v in data['pokemon_data.json'].items() if not k.startswith('メガ')}

# 結果を新しいJSONファイルに保存
with open('pokemon_data.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
