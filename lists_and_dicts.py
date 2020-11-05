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

list_1 = ['c', 'о', 'с', 'и']
list_2 = ['ж', 'о', 'п', 'у']
first_counter = 0
q_counter = 0
second_counter = 0
new_list = list()
for i in list_1:
    if first_counter % 2 == 0:
        new_list.append(list_1[first_counter])
        print(new_list, i, first_counter)
        continue
    else:
        print(new_list, i, first_counter)
        continue
# for j in list_2:
#     if q_counter % 2 != 0:
#         if first_counter % 2 != 0:
#             new_list.append(list_1[first_counter])
#             first_counter += 1
#             q_counter += 1
#         else:
#             q_counter += 1
# print(q_counter)
#
#     if q_counter % 2 == 0:
#         if second_counter % 2 == 0:
#             new_list.append(list_2[second_counter])
#             q_counter += 1
#             second_counter += 1
#         else:
#             q_counter += 1
# print(new_list)
