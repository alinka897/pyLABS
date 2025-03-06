"""
Вычислить LOGa(b), используя
полином Лагранжа
"""

def precision(base, arg):
    cur_L = L(1, base, arg)
    prev_L = L(2, base, arg)
    prev_delta = abs(cur_L - prev_L)
    for n in range(3, 20):
        cur_L = L(n, base, arg)
        delta = abs(cur_L - prev_L)
        print(prev_delta, delta, prev_L, cur_L)
        if abs(delta - prev_delta) >= 0.07:
            return prev_L
        prev_L = cur_L
        prev_delta = delta

def F(n, i, arg, xs):
    """
    n - кол-во узлов
    i - данный икс
    arg - аргумент искомой функции
    xs - список абсцисс узлов
    """
    mul = 1
    for j in range(n+1):
        if j==i:
            continue
        mul *= (arg - xs[j])/(xs[i] - xs[j])   
    return mul
    
def L(n, base, arg):
    """
    base - основание логарифма
    dots - список с точками(кортежами)
    """
    dots  = [(base**y,y) for y in range(1,100)]
    xys = sorted(dots, key=lambda xy: (abs(arg-xy[0]), xy[1]))
    xys = xys[:n+1]
    print(xys)
    sum = 0
    xs = [xy[0] for xy in xys]
    ys = [xy[1] for xy in xys]
    for i in range(n+1):
        sum += ys[i]*F(n, i, arg, xs)
    return sum


def main():
    base = 0
    while (base <= 1):
        base = int(input("Введите основание логарифма: "))
    arg = base
    while (arg <= base):
        arg = int(input("Введите арумент логарифма: "))
    print(precision(base, arg))


main()
