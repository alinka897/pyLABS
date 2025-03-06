from random import randint, shuffle
list_randoms = [randint(-100,100) for i in range(100)]
for i in range(10):
    shuffle(list_randoms)
print(list_randoms)
left = -101
right = 101
while left >= right or not(-100 <= left < 100) or not(-100 < right <= 100):
    left, right = input("Введите границы через пробел(-100, 100): ").split()
    left, right = int(left), int(right)
    if left == right:
        break
print(list_randoms) 
list_borders = [x for x in list_randoms if x in range(left, right + 1)]
print(list_borders)
list_even = [x for x in list_randoms if abs(x)%2 == 0]
print(list_even)
print(sum(map(abs, list_even)))


