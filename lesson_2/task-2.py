num = input('Введите натуральноеое число: ')
chet_count = 0
nechet_count = 0
for n in num:
    if int(n) % 2 == 0:
        chet_count += 1
    else:
        nechet_count += 1
print(f'В числе {num} {chet_count} чётных цифр и {nechet_count} нечётных цифр.')
