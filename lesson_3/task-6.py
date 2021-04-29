import random

SIZE = 10
MIN_ELEM = 0
MAX_ELEM = 100
array = [random.randint(MIN_ELEM, MAX_ELEM) for _ in range(SIZE)]
print(f'Массив: {", ".join(map(str, array))}')

min_item = MAX_ELEM
min_index = 0
max_item = MIN_ELEM
max_index = 0
for i, item in enumerate(array):
    if item > max_item:
        max_item = item
        max_index = i
    if item < min_item:
        min_item = item
        min_index = i

summa = 0
if min_index <= max_index:
    for i in array[min_index+1:max_index]:
        summa += i
else:
    for i in array[max_index+1:min_index]:
        summa += i
print(f'Сумма элементов между минимальным ({min_item}) и максимальным ({max_item}) элементами равна {summa}.')
