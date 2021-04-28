operation = input('Введите операцию(+, -, *, /) или "0" чтобы закончить: ')
while operation != '0':
    a, b = map(int, input('Введите два числа через пробел: ').split())
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        if b == 0:
            result = 'Ошибка! Деление на ноль!'
        else:
            result = a / b
    else:
        result = 'Такой арифметической операции не существует!'
    print(result)
    operation = input('Введите операцию(+, -, *, /) или "0" чтобы закончить: ')
