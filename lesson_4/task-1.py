"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
"""

import timeit
import cProfile


# a = int(input('Введите число: '))


def recursive_reverse(num, new_num=''):
    if not num:
        return int(new_num)
    else:
        new_num += str(num)[-1]
        return recursive_reverse(str(num)[:-1], new_num)


print(timeit.timeit('recursive_reverse(1234)', number=100, globals=globals()))  # 0.0004960000000000034
print(timeit.timeit('recursive_reverse(12345)', number=100, globals=globals()))  # 0.0005870000000000042
print(timeit.timeit('recursive_reverse(123456)', number=100, globals=globals()))  # 0.0006826000000000054
print(timeit.timeit('recursive_reverse(1234567)', number=100, globals=globals()))  # 0.0007669000000000009
print(timeit.timeit('recursive_reverse(12345678)', number=100, globals=globals()))  # 0.0008439999999999975
cProfile.run('recursive_reverse(12345678)')


# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#    9/1    0.000    0.000    0.000    0.000 task-1.py:10(recursive_reverse)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def loop_reverse(num):
    new_num = ''
    for i in str(num)[::-1]:
        new_num += i
    return int(new_num)


print(timeit.timeit('loop_reverse(1234)', number=100, globals=globals()))  # 0.00017789999999999473
print(timeit.timeit('loop_reverse(12345)', number=100, globals=globals()))  # 0.00017239999999999617
print(timeit.timeit('loop_reverse(123456)', number=100, globals=globals()))  # 0.0002908000000000008
print(timeit.timeit('loop_reverse(1234567)', number=100, globals=globals()))  # 0.0002727000000000007
print(timeit.timeit('loop_reverse(12345678)', number=100, globals=globals()))  # 0.00022230000000000166
cProfile.run('loop_reverse(12345678)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 task-1.py:36(loop_reverse)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def standard_reverse(num):
    num = str(num).split()
    num.reverse()
    return int(''.join(num))


print(timeit.timeit('standard_reverse(1234)', number=100, globals=globals()))  # 8.980000000000099e-05
print(timeit.timeit('standard_reverse(12345)', number=100, globals=globals()))  # 7.82999999999999e-05
print(timeit.timeit('standard_reverse(123456)', number=100, globals=globals()))  # 8.009999999999962e-05
print(timeit.timeit('standard_reverse(1234567)', number=100, globals=globals()))  # 8.029999999999843e-05
print(timeit.timeit('standard_reverse(12345678)', number=100, globals=globals()))  # 8.19000000000028e-05
cProfile.run('standard_reverse(12345678)')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task-1.py:57(standard_reverse)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
#      1    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
