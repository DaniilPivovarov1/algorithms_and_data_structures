from collections import deque

a = deque(input('Введите первое шестнадцатеричное число: ').upper())
b = deque(input('Введите второе шестнадцатеричное число: ').upper())

sixteen_numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

decimal_numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                   'C': 12, 'D': 13, 'E': 14, 'F': 15}

first, second = a.copy(), b.copy()
if len(second) > len(first):
    first, second = second, first

second.appendleft('0' * (len(first) - len(second)))

sum_res = deque()
repletion = 0
while len(first) != 0:
    first_num = decimal_numbers[first.pop()]
    second_num = decimal_numbers[second.pop()]

    res = first_num + second_num + repletion

    if res >= 16:
        repletion = 1
        res -= 16
    else:
        repletion = 0

    sum_res.appendleft(sixteen_numbers[res])

if repletion == 1:
    sum_res.appendleft('1')

print(f'{"".join(a)} + {"".join(b)} = {"".join(sum_res)}')
