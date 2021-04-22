a, b, c = map(int, input('Введите три числа через пробел: ').split())
if b > a > c or c > a > b:
    print(a)
elif a > b > c or c > b > a:
    print(b)
else:
    print(c)
