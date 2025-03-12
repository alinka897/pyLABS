"""
Задать список из строк произвольной длины (5-8) из русских букв.
Просортировать и вывести список по разным типам сортировки.
"""

from random import randint, choice

def alph_sort(len_d):
    alpha = [chr(x) for x in range(ord('а'), ord('я'))]
    ls = list()    
    for item in range(len_d):
        string = ''.join([choice(alpha) for i in range(randint(5,8))])
        ls.append(string)
    print(ls)
    print(f"Лексикографическая сортировка: {sorted(ls)}")
    print(f"Сортировка по длине: {sorted(ls, key=len)}")

if __name__ == "__main__":
    len_d = int(input("Введите длину списка: "))
    alph_sort(len_d)
