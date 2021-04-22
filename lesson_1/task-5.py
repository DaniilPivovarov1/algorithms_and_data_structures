a, b = input('Введите первую букву: '), input('Введите вторую букву: ')
alpha = 'abcdefghijklmnopqrstuvwxyz'

a_position = alpha.index(a) + 1
b_position = alpha.index(b) + 1
letters_between_count = b_position - a_position - 1
print(f'Позиция первой буквы в алфавите = {a_position}, позиция второй буквы в алфавите = {b_position}')
if (letters_between_count == 1 or letters_between_count == 21) and letters_between_count != 11:
    print(f'Между ними стоит {b_position - a_position - 1} буква')
elif 1 < letters_between_count < 6 or 21 < letters_between_count < 25:
    print(f'Между ними стоит {b_position - a_position - 1} буквы')
else:
    print(f'Между ними стоит {b_position - a_position - 1} букв')
