print('Заполните матрицу 5x3:')
matrix = [list(map(int, input().split())) for _ in range(5)]
for i in range(5):
    summa = 0
    for j in matrix[i]:
        summa += j
    matrix[i].append(summa)
for i in matrix:
    print(' '.join(map(str, i)))
