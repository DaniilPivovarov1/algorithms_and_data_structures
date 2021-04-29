import random

SIZE = 10
MIN_ELEM = -20
MAX_ELEM = 20
array = [random.randint(MIN_ELEM, MAX_ELEM) for _ in range(SIZE)]

max_negative_item = MIN_ELEM
max_negative_item_index = 0
for i in range(len(array)):
    if 0 > array[i] > max_negative_item:
        max_negative_item = array[i]
        max_negative_item_index = i

print(f'Самое большое отрицательное число в массиве {", ".join(map(str, array))} - это {max_negative_item} и оно стоит на {max_negative_item_index} позиции.')
