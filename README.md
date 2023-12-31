# pokemon-go-data

ポケモンGOの各種データを取得するための処理を集めたレポジトリ．

## メインファイルの説明

* WazaScraping.py：わざ1わざ2に関するデータを取得する
* PokemonLinkScraping.py：各ポケモンの詳細がわかるURLを集めたデータを取得する
* Pokemon_WazaData_GetDaze.py：各ポケモン詳細URLデータから，各ポケモンの覚える技データを取得する

## 環境構築

### 前提

```sh
$ sw_vers
ProductName:		macOS
ProductVersion:		13.5.1
BuildVersion:		22G90
$ python3 -V
Python 3.11.4
```

```python
$python3 -m venv .venv
$source .venv/bin/activate
$pip install -r requirement.txt
```

## CSVからJSONに変換

今後必要に応じてCSVからJSONデータに変換するよう組み込む。
とりあえず，以下のサイトで変換のみ実施。
https://www.aconvert.com/jp/document/csv-to-json/

※変換前に行名が3行に渡っているため1行に直す。（TODO:将来的にはこの手動変換も組み込みたい...。）

* ノーマルわざ：「No,わざ,タイプ,威力,エネルギー充填,秒数,ダメージ発生時間(秒):開始,ダメージ発生時間(秒):終了,威力,PvPエネルギー充填,ターン数」
* スペシャルわざ：「No,わざ,タイプ,威力,エネルギー充填,秒数,ダメージ発生時間(秒):開始,ダメージ発生時間(秒):終了,威力,PvPエネルギー充填,追加効果,発生確率」

