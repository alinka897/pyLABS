"""
18. Задать словарь из 4-х айтемов. Значение каждого
айтема - список из 5 целочисленных элементов.
Программа должна вывести тот айтем, у которого сумма
элементов значения минимальна.
"""


def min_item(dict_with_ls):
    for k, v in dict_with_ls.items():
        if v == min(dict_with_ls.values(), key=sum):
            print(k, v)


if __name__ == '__main__':
    from random import randint
    d = {x: [randint(-100, 100) for i in range(5)] for x in range(4)}
    print(d)
    min_item(d)
