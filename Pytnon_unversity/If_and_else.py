# Задание 28
a = input('Введите трёхзначное число - ')
try:
    pr = int(list(a)[0]) * int(list(a)[1]) * int(list(a)[2])
    s = int(list(a)[0]) + int(list(a)[1]) + int(list(a)[2])
    if pr < int(a):
        print(f"Произведение чисел меньше числа а - {pr}")
    else:
        print(f"Произведение чисел больше числа а - {pr}")
    if s % 5 == 0:
        print(f'Сумма кратна пяти - {s}')
    else:
        print(f'Сумма не кратна пяти - {s}')
except Exception as error:
    print('Нужно ввести трёхзначное ЧИСЛО')
