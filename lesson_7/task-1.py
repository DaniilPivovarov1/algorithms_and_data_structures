import random


def reversed_bubble_sort(array):
    i = 1
    while i < len(array):
        for j in range(len(array) - i):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        i += 1
    return array


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
data = [random.randrange(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(data)
print(reversed_bubble_sort(data))
