import collections

pred_count = int(input('Введите количество предприятий: '))
pred_dict = collections.defaultdict()
summa = 0
for i in range(1, pred_count + 1):
    loop_key = input(f'Введите название {i}-ого предприятия: ')
    loop_value = [int(input(f'Введите прибыль {i}-ого предприятия за {j}-ый квартал: ')) for j in range(1, 5)]
    pred_dict[loop_key] = loop_value
    summa += sum(loop_value)

av = summa / pred_count
before_av = []
after_av = []
for key, value in pred_dict.items():
    if sum(value) < av:
        before_av.append(key)
    elif sum(value) > av:
        after_av.append(key)

print()
print(f'Названия предприятий, чья прибыль ниже среднего: {", ".join(before_av)}.')
print(f'Названия предприятий, чья прибыль выше среднего: {", ".join(after_av)}.')
