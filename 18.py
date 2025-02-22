#Заполнить словарь списками и вывести тот айтем, у которого сумма наименьшая
import random

def func():
    d = {x: [random.randint(-100,100) for i in range(5)] for x in range(4)}
    print(d)
    for k,v in d.items():
        if v==min(d.values(), key = sum):
            return (k,v)
print(func())
