"""
Set a list with strings (len 5-8).
Sort the list in different ways.
"""

from random import randint, choice
from collections import deque

def alph_sort(len_d):
    alpha = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    deck = deque()    
    for item in range(int(len_d)):
        string = ''.join([choice(alpha) for i in range(randint(5,8))])
        deck.append(string)
    print(deck)
    print(f"Лексикографическая сортировка: {sorted(deck)}")
    print(f"Сортировка по длине: {sorted(deck, key=len)}")

len_d = input("Введите длину списка: ")
alph_sort(len_d)
