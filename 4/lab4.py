"""
Записать два разных файла, т.е. два потока рандомных чисел —
по одному в строку, диапазон -50 +50.
Сделать 10 строк и вывести параллельно в 2 столбца. 
"""
from random import randint

def func():
    with open('file1.txt', 'w') as f1, open('file2.txt', 'w') as f2:
        for line in range(10):
            a = str(randint(-50,50))
            b = str(randint(-50,50))
            f1.write(a + '\n')
            f2.write(b + '\n')
            print(a + '\t' + b)

if __name__ == "__main__":
    func()
