n = int(input('Введите n: '))
print(f"{' + '.join(str(i) for i in range(1, n + 1))} = ", n, '(', n, ' + 1) / 2', sep='')
print(f'{sum(i for i in range(1, n + 1))} = {int(n * (n + 1) / 2)}')
