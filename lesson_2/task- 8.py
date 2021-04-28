finding_num = int(input('Ввведите число, которое необходимо посчитать: '))
posl_len = int(input('Введите длину последовательности: '))
c = 0
for i in range(1, posl_len + 1):
    num = int(input(f'Введите {i}ое число последовательности: '))
    if num == finding_num:
        c += 1
print(f'В данной последовательности чисел число {finding_num} встречается {c} раз.')
