posl_len = int(input('Введите длину последовательности: '))
max_sum = 0
max_num = 0
for i in range(1, posl_len + 1):
    num = int(input(f'Введите {i}ое число последовательности: '))
    num_sum = num // 100 + num % 100 // 10 + num % 10
    if num_sum > max_sum:
        max_sum = num_sum
        max_num = num
print(f'Число с максимальной суммой чисел: {max_num} и его сумма равна {max_sum}.')
