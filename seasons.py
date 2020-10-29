number = int(input('Введите номер месяца - '))
if number == 3 or 4 or 5:
    print('Весна')
elif number == 6 or 7 or 8:
    print('Лето')
elif number == 9 or 10 or 11:
    print('Осень')
elif number == 12 or 1 or 2:
    print('Зима')
else:
    print(f'Неверный формат данных - {Exception}')