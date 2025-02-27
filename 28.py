"""
Set a list with strings (len 5-8).
Sort the list by different types.
"""

import random
from collections import deque

alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ls = []
string = ''
for item in range(random.randint(5,15)):
    for i in range(random.randint(5,8)):
        string += random.choice(alpha)
    ls.append(string)
    string = ''
deck = deque(ls)
print(deck)
print(f"Лексикографическая сортировка: {sorted(deck)}")
print(f"Сортировка по длине: {sorted(deck, key=len)}")
