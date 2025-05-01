import random
import csv
import re

with open("pokemon_list.csv", "r", encoding="utf-8") as f:
        r = csv.reader(f)
        pokemons_list = [row for row in r]
num = 0
pokemon ='ピカチュウ'
taipu = ["でんき","なし"]
type1 = "指定なし"
type2 = "指定なし"

def select(taipu1, taipu2):
    message = str(pokemons_list[0][0])
    return message

select(type1,type2)

def call_ai():
    pass

def is_katakana(text,messaged):
    p = re.compile('[\u30a1-\u30fa\u30fc]+')

    if not p.fullmatch(text):
        message ="入力はカタカナのみです。"
        return message

    else:
        return messaged


def hantei(user_input):
    global num
    global pokemon
    if len(user_input) == 5:
        num += 1
        if user_input == pokemon:
            content = "正解！<br>"
            message =content+ str(num) + "手目で正解！"
        else:
            content = "残念！<br>"
            message =content + "間違えです。"
        for i in range(len(user_input)):
            if user_input[i] == pokemon[i]:
                message += '<div class="text-white bg-success d-inline">' + user_input[i] + '</div>'
            else:
                message += '<div class="text-white bg-secondary d-inline">' + user_input[i] + '</div>'
    else:
        message = "5文字の文字を入力してください。"
    message = is_katakana(user_input,message)
    return message

def debug_message(user_input, request):
    global pokemon
    message=[]
    message.append("───デバッグモード───<br>")
    message.append("user_input:"+request['user_input'])
    message.append("option1:"+request['options1'])
    message.append("option2:"+request['options2'])
    message.append("debug:"+request['debug'])
    message.append("current_message:"+request['current_message'])
    message.append(pokemon)
    message.append("")
    message.append("─デバッグモード─")

    full_text=""
    for str in message:
        full_text+=str + "<br>"

    return full_text

def reset(taipu1, taipu2):
    global num
    global pokemon
    global taipu
    global type1
    global type2
    num = 0
    pokemon ='ピカチュウ'
    taipu = ["でんき","なし"]
    type1 = "指定なし"
    type2 = "指定なし" 
    message = "リセットしました。<br>"
    select(taipu1,taipu2)
    return message

def hint():
    message = "test"
    return message

def vs(user_input):
    message = "test"
    return message

def helps():
    title = "＊遊び方＊<br>"
    explains ="入力欄からポケモンの名前を予測して入力→送信<br>"
    tips = "[機能一覧]<br>・ヒント:ポケモンのタイプがわかるよ<br>・正解表示:答えがわかるよ<br>・リセット:正解をリセットするよ<br>・二つのプルダウンメニューからポケモンのタイプを絞れるよ"
    message = title+explains+tips
    return message

def answer():
    message = pokemon
    return message
