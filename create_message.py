import random # ランダムな値を生成するためのモジュール
import csv # CSVファイルを読み込むためのモジュール
import re # 正規表現を扱うためのモジュール（未使用だが、文字列チェックなどに使える）

# ポケモンのリストをCSVファイルから読み込む
with open("pokemon_list.csv", "r", encoding="utf-8") as f:
    r = csv.reader(f)
    pokemons_list = [row for row in r]  # 各行をリストとして読み込み、pokemons_listに格納

# 初期化：ポケモン番号、名前、タイプ
num = 0
pokemon = 'ピカチュウ'
taipu = ["でんき", "なし"]  # タイプ1とタイプ2（タイプ2がない場合は "なし"）

# ユーザーが選択したタイプ（初期状態では「指定なし」）
type1 = "指定なし"
type2 = "指定なし"

# タイプに基づいてポケモンを選択する関数（仮実装）
def select(taipu1, taipu2):
    message = "test"  # 実際にはここでタイプに合うポケモンを選ぶ処理を記述
    return message

# 関数を一度呼び出している
select(type1, type2)

# AIを呼び出す関数（未実装）
def call_ai():
    pass

# カタカナかどうかを判定する関数（未実装）
def is_katakana(text):
    pass

# ユーザーの入力を判定する関数（未実装）
def hantei(user_input):
    message = "test" 
    return message

# デバッグ用のメッセージを生成する関数（未実装）
def debug_message(user_input, request):
    message = "test" 
    return message
        
# ゲームをリセットする関数（未実装）
def reset(taipu1, taipu2):
    message = "test"  
    return message

# ヒントを表示する関数（仮実装）
def hint():
    message = "test"
    return message

# AIとの対戦処理を行う関数（未実装）
def vs(user_input):
    message = "test"  
    return message
        
# 遊び方メッセージを返す関数（未実装）
def helps():
    message = "test"      return message

# 正解を表示する関数（未実装）
def answer():
    message = "test" 
    return message
