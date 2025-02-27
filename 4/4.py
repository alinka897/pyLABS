"""
Fill 2 files with random numbers
and print them in 2 columns 
"""
import random

def func(n, m):
    f1 = open(n, 'w')
    f2 = open(m, 'w')
    for line in range(10):
        a = str(random.randint(-50,50))
        b = str(random.randint(-50,50))
        f1.write(a + '\n')
        f2.write(b + '\n')
        print(a + '\t' + b)
    f1.close()
    f2.close()

f1 = input("Enter the path to the first file: ")
f2 = input("Enter the path to the second file: ")
func(f1, f2)
