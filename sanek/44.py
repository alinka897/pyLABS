import random

list_randoms = [random.randint(0,50) for i in range(100)]
for n in range(10):
    l = list_randoms[10*n:10*(n+1)]
    print(l)
    counter = 0
    for x in l:
        if 9 - x >= 0:
            counter += 1
    print(counter)
