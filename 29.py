'''
Засунуть вручную этот путь как список, кот состоит из
подстрок разной длины, вывести их, найти самую минимальную
по длине подстроку и дать индекс ее начала
'''

from collections import deque

def get_min_index():
    path = "/usr/share/nvim/runtime"
    strings = deque(path.split('/'))
    strings.popleft()
    for i in strings:
        print(i, end = ' ') if i != strings[-1] else print(i)
    for i, v in enumerate(strings):
        if v == min(strings, key=len):
            print(i, v)
    
    min_val = min(strings, key=len)
    print(path.find(min_val), min_val)
    

get_min_index()
