"""
4. Записать два разных файла, т.е. два потока рандомных чисел —
по одному в строку, диапазон -50 +50.
Сделать 10 строк и вывести параллельно в 2 столбца.
"""


def rnum2f(p, q, /, lines=10):
    from random import randint
    with open('file1.txt', 'w+') as f1, open('file2.txt', 'w+') as f2:
        for line in range(lines):
            a, b = str(randint(p, q)), str(randint(p, q))
            f1.write(a + '\n')
            f2.write(b + '\n')
        f1.seek(0)
        f2.seek(0)
        for line in range(lines):
            line1, line2 = f1.readline().strip(), f2.readline().strip()
            print(line1 + '\t' + line2)


if __name__ == "__main__":
    rnum2f(-50, 50)
