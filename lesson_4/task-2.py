import timeit
import cProfile


def ith_simple_number_with(n, y):
    a = [0] * n
    for i in range(n):
        a[i] = i

    a[1] = 0

    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    return b[y - 1]


print(timeit.timeit('ith_simple_number_with(15, 5)', number=100, globals=globals()))  # 0.0005956000000000017
print(timeit.timeit('ith_simple_number_with(20, 5)', number=100, globals=globals()))  # 0.0007647000000000001
print(timeit.timeit('ith_simple_number_with(25, 5)', number=100, globals=globals()))  # 0.0009648000000000018
cProfile.run('ith_simple_number_with(20, 5)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task-2.py:5(ith_simple_number)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def ith_simple_number_without(n, y):
    simple_numbers = []
    for i in range(2, n):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag:
            simple_numbers.append(i)
    return simple_numbers[y - 1]


print(timeit.timeit('ith_simple_number_without(15, 5)', number=100, globals=globals()))  # 0.0008004999999999991
print(timeit.timeit('ith_simple_number_without(20, 5)', number=100, globals=globals()))  # 0.0010179000000000021
print(timeit.timeit('ith_simple_number_without(25, 5)', number=100, globals=globals()))  # 0.0015430999999999986
cProfile.run('ith_simple_number_without(20, 5)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task-2.py:41(ith_simple_number_without)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
