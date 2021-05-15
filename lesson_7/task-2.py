import random


def sliyanie_sort(array):
    if len(array) <= 1:
        return array
    else:
        left = sliyanie_sort(array[:len(array) // 2])
        right = sliyanie_sort(array[len(array) // 2:])
        li = ri = 0
        while len(left) > li and len(right) > ri:
            if left[li] < right[ri]:
                array[li + ri] = left[li]
                li += 1
            else:
                array[li + ri] = right[ri]
                ri += 1
        while len(right) > ri:
            array[li + ri] = right[ri]
            ri += 1
        while len(left) > li:
            array[li + ri] = left[li]
            li += 1

    return array


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
data = [random.randrange(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(data)
print(sliyanie_sort(data))
