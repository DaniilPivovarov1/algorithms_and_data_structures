size = input('Введите размеры матрицы в формате y x: ')
y_size, x_size = int(size.split()[0]), int(size.split()[1])
print('Заполните эту матрицу:')
matrix = [list(map(int, input().split())) for _ in range(y_size)]
min_li = []
for j in range(x_size):
    min_st = int('9' + '9' * 15)
    for i in range(y_size):
        if matrix[i][j] < min_st:
            min_st = matrix[i][j]
    min_li.append(min_st)

max_in_min = int('-9' + '9' * 15)
for i in min_li:
    if i > max_in_min:
        max_in_min = i
print(max_in_min)
