import random

a, b = input('Введите начало границы: '), input('Введите конец границы: ')
alpha = 'abcdefghijklmnopqrstuvwxyz'
if '.' not in a:
    if a in alpha:
        print(alpha[random.randint(alpha.index(a), alpha.index(b))])
    else:
        print(random.randint(int(a), int(b)))
else:
    c = random.randint(1, int(float(b) - float(a)))
    print(random.random() + float(a) * c)
