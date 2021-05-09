"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
"""

from sys import getsizeof

a = 3486


def recursive_reverse(num, new_num=''):
    if not num:
        return int(new_num)
    else:
        new_num += str(num)[-1]
        return recursive_reverse(str(num)[:-1], new_num)


result = recursive_reverse(a)
print(f'Всего под переменные было выделено {getsizeof(a) + getsizeof(result)} байтов')  # 28 байтов
# Версия python: 3.8
# Разрядность OC: 64 бита
