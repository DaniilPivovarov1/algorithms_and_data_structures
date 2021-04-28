n = int(input('Введите количество элементов (n): '))
current_num = 1
summa = current_num
for i in range(n - 1):
    current_num *= -0.5
    summa += current_num

print(summa)
