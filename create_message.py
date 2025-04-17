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
    message = "test"
    return message

select(type1,type2)

def call_ai():
    pass

def is_katakana(text):
    pass

def hantei(user_input):
    message = "test"
    return message

def debug_message(user_input, request):
    message = "test"
    return message

def reset(taipu1, taipu2):
    message = "test"
    return message

def hint():
    message = "test"
    return message

def vs(user_input):
    message = "test"
    return message

def helps():
    message = "test"
    return message

def answer():
    message = "test"
    return message