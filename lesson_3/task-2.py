first_array = list(map(int, input('Введите элементы массива через пробел: ').split()))
second_array = [str(i) for i in range(len(first_array)) if first_array[i] % 2 == 0]
print(f"Массив с индексами чётных элементов первого массива: {', '.join(second_array)}")
