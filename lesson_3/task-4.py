import random

SIZE = 10
MIN_ELEM = 0
MAX_ELEM = 10
array = [random.randint(MIN_ELEM, MAX_ELEM) for _ in range(SIZE)]

max_count = MIN_ELEM
max_count_value = 0
for i in array:
    if array.count(i) > max_count:
        max_count = array.count(i)
        max_count_value = i
print(f'Больше всего в массиве {", ".join(map(str, array))} встречается число {max_count_value}')
