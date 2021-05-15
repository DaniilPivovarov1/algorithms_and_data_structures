import random


def median_get(array):
    if len(array) == 1:
        return array[0]
    else:
        array.remove(min(array))
        array.remove(max(array))
        return median_get(array)


SIZE = 4
MIN_ITEM = -100
MAX_ITEM = 100
data = [random.randrange(MIN_ITEM, MAX_ITEM) for _ in range(2 * SIZE + 1)]
print(data)
print(median_get(data))

