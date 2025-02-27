"""
Объяснить алгоритм,
переделать, чтобы файл читался целиком
"""
from collections import deque
from collections import Counter

delta = int(input('Введите длину новой последовательности (2-8): '))
st_final = [] # for final result
try:
    with open('text.txt') as f:
        my_file = f.readlines()
        for line in my_file:
            for slowo in line.split():
                if len(slowo) < delta:
                    continue
                elif slowo[0].isdigit() is True:
                    continue
                else:
                    if slowo[-1] in ',.?!:;\'"':
                        slowo = slowo[:-1]
                    if slowo[-2:] == '..':
                        slowo = slowo[:-2]
                    if slowo[0] in '"\'':
                        slowo = slowo[1:]
                    slowo = slowo.lower()
                    slowo_d = deque(slowo)
                    while len(slowo_d) >= delta:
                        st_final.append(''.join(slowo_d)[0:delta])
                        slowo_d.popleft()
except FileNotFoundError:
    print('Нет такого файла')

print(Counter(st_final).most_common(68))
