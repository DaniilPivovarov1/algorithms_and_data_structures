"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
"""

from sys import getsizeof

a = 3486


def loop_reverse(num):
    new_num = ''
    for i in str(num)[::-1]:
        new_num += i
    return int(new_num)


result = loop_reverse(a)
print(f'Всего под переменные было выделено {getsizeof(a) + getsizeof(result)} байтов')  # 28 байтов
# Версия python: 3.8
# Разрядность OC: 64 бита
