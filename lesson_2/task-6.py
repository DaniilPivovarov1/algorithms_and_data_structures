import random
r_num = random.randint(0, 100)
for i in range(10):
    user_num = int(input('Введите число: '))
    if r_num == user_num:
        print('Вы угадали!')
        break
    elif i == 9:
        print(f'Все попытки истекли. Правильный ответ: {r_num}')
    elif r_num > user_num:
        print('Загаданное число больше введённого')
    else:
        print('Загаданное число меньше введённого')
