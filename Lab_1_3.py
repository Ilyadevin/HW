new_index = input("Введите числа через запятую - ")
list_ints = new_index.split(', ')
result = 1
for i in list_ints:
    if int(i) < 10:
        result = result * int(i)
    else:
        pass
print(f"Произведение чисел меньше 10 - {result}")
