def recursive_reverse(num, new_num=''):
    if not num:
        return new_num
    else:
        new_num += str(num)[-1]
        return recursive_reverse(str(num)[:-1], new_num)


a = int(input('Введите число: '))
print(int(recursive_reverse(a)))
