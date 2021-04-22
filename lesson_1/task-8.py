year = int(input('Введите год: '))
if year % 400 == 0:
    print('Этот год високосный.')
else:
    if year % 100 == 0:
        print('Этот год не високосный')
    else:
        if year % 4 == 0:
            print('Этот год високосный.')
        else:
            print('Этот год не високосный')
