#Заполнить два файла и вывести их содержимое в два столбца
import random
def func(n,m):
    f1 = open(n, 'w')
    f2 = open(m, 'w')
    for line in range(10):
        a = str(random.randint(-50,50))
        b = str(random.randint(-50,50))
        f1.write(a)
        f2.write(b)
        print(a+"\t"+b)
    f1.close()
    f2.close()
f1 = input("Введите путь к первому файлу: ")
f2 = input("Введите путь ко второму файлу: ")
func(f1,f2)
