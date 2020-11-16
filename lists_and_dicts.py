# Задача 28
# whole_integer = [1, 2, 3, 4, 5,
#                  6, 7, 8, 9, 10,
#                  11, 12, 13, 14, 15,
#                  16, 17, 299, 78]
# i_counter = 0
# sum_odd = 0
# sum_even = 0
# for i in whole_integer:
#     i_counter += 1
#     try:
#         if i_counter % 2 == 0:
#             sum_odd += whole_integer[i_counter]
#         else:
#             sum_even += whole_integer[i_counter]
#     except IndexError as error:
#         pass
# print(f"Сумма элементов с четными индексами - {sum_odd}\n"
#       f"Сумма элементов с нечетными индексами -  {sum_even}")
# print()
# print(f'Остаток от деления суммы элементов с четным индексом на '
#       f'сумму эелементов с нечетным индексом - {sum_odd % sum_even}')
# integer_in_binary = '0b' + input('Введите целое число в двоичное системе - ')
# try:
#     converted_integer = int(integer_in_binary, 2)
#     print(f'Число {integer_in_binary} в десятичной системе - {converted_integer}')
# except Exception as error:
#     print(f'Число в двоичной системе не целое!\n'
#           f'{error}')

first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
second_list = [1, 3, 6, 7, 8, 9, 10, 11, 12, 13, 19]
for i in range(len(first_list)):
    for j in range(len(second_list)):
        if first_list[i] == second_list[j]:
            first_list[i] = 0
        else:
            continue
print('Массив с измененными данными:')
for answer in first_list:
    print(answer, end=', ')
