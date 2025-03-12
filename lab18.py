"""
Задать словарь из 4-х айтемов. Значение каждого
айтема - список из 5 целочисленных элементов.
Программа должна вывести тот айтем, у которого сумма
элементов значения минимальна.
"""

from random import randint

def min_item():
    d = {x: [randint(-100,100) for i in range(5)] for x in range(4)}
    print(d)
    for k, v in d.items():
        if v == min(d.values(), key = sum):
            print(k, v)

if __name__ == '__main__':  
    min_item()
