import random
import csv
import re

with open("pokemon_list.csv", "r", encoding="utf-8") as f:
        r = csv.reader(f)
        pokemons = [row for row in r]
num = 0
pokemon ='test'
taipu = ["でんき","なし"]

def select():
    global pokemon, taipu
    pokemon = pokemons[random.randint(0,276)]
    pokemon = pokemon[0]
select()
#print(pokemon)

def call_ai():
    ai_poke = pokemons[random.randint(0,276)]
    ai_poke_name = ai_poke[0]
    ai_poke_type1 = ai_poke[1]
    ai_poke_type2 = ai_poke[2]
    return ai_poke_name
#print(call_ai())

def is_katakana(text):
    pattern = r'^[ァ-ヶー]+$'
    if re.match(pattern, text):
        return True
    else:
        return False

def hantei(user_input,debug_flag):
    global num,pokemon
    num += 1
    if user_input == pokemon:
        message = '{}手目で正解!!!'.format(num) + '\nおめでとう！'
    elif is_katakana(user_input) != True:
        num -= 1
        message = 'ポケモン名は全角カタカナだよ'
    else:
        message ='ハズレ!!!' + '\nまた挑戦してね！' 
        #message = pokemon
    if debug_flag == True:
        message = "valid is {}: ".format(pokemon) + message
    return message

def reset_num():
    global num
    num = 0
    message = "リセット完了"
    select()
    return message

def hint():
    message = "helpモード\nTEST"
    return message

def vs(user_input, debug_flag):
    global num,pokemon
    ai_poke = call_ai()
    user_result = hantei(user_input, debug_flag)
    if "おめでとう" in user_result:
        message = user_result
    elif ai_poke == pokemon:
        message = "{}手目でAIの勝ち！！正解は {}".format(num,pokemon)
    else:
        message = "はずれ！！　User:" + user_input + " AI:" + ai_poke
        if debug_flag == True:
            message = "valid is {}: ".format(pokemon) + message
    if is_katakana(user_input) != True:
        num -= 1
        message = 'ポケモン名は全角カタカナだよ'
 #   message = "vs mode"
    return message


def ai(user_input, debug_flag):
    message = "AIモード"
    return message


#Debug command
#for i in range(5):
#    print(hantei("ピカチュウ",True))
#print(hantei("TEST",True))
#print(hantei(pokemon,True))
