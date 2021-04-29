import random

SIZE = 10
MIN_ELEM = 0
MAX_ELEM = 50
array = [random.randint(MIN_ELEM, MAX_ELEM) for _ in range(SIZE)]
print(f'Массив: {", ".join(map(str, array))}')

pre_min_item = MAX_ELEM
min_item = MAX_ELEM
for i in array:
    if i < min_item:
        min_item = i
array.remove(min_item)
for i in array:
    if i < pre_min_item:
        pre_min_item = i

print(f'В данном массиве два наименьших элемента - это {min_item} и {pre_min_item}')
