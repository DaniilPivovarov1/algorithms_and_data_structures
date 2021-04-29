import random

SIZE = 10
MIN_ELEM = 0
MAX_ELEM = 100
array = [random.randint(MIN_ELEM, MAX_ELEM) for _ in range(SIZE)]
print(f'Старый массив: {", ".join(map(str, array))}')

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

array[min_index], array[max_index] = array[max_index], array[min_index]
print(f'Новый массив: {", ".join(map(str, array))}')
