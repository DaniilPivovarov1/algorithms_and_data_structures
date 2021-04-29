c_li = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            c_li[j - 2] += 1

for i in range(len(c_li)):
    print(f'{i + 2}-{c_li[i]}')
