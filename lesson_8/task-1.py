def find_strings(s):
    variants = []
    for i in range(1, len(s) + 1):
        for j in range(len(s) - i + 1):
            variants.append(s[j:j+i])
    return variants


my_s = 'abcd'
result = find_strings(my_s)
print(f'В строке "{my_s}" {len(result)} различных подстрок.\nЭто строки {result}.')
