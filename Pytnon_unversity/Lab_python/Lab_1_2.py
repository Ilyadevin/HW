new_index = input("Введите символы через запятую - ")
list_types = new_index.split(', ')
list_of_ints = []
for i in list_types:
    try:
        if int(i) % 2 == 0:
            list_of_ints.append(i)
        else:
            pass
    except Exception as error:
        print(f'Неверный формат ввода {error}')
print(f'Четные числа - {list_of_ints}')
