# variable_for_task_1 = input('Введите переменную для задания 1 - ')
#
#
# def task_1(n):
#     numbers = [2, 5, 13,
#                29, 31, ]  # Список с простыми числами (простое число - число, которое делится ТОЛЬКО на само себя и 1
#     mp = list()
#     answers = list()
#     for p in numbers:
#         try:
#             q = 2 * p - 1
#             mp.append(q)
#         except Exception as error:
#             print(error)
#             raise
#     for number in mp:
#         try:
#             n = int(n)
#             if int(n) > number:
#                 answers.append(number)
#                 print(f'Число {n} больше числа {number}')
#             else:
#                 print(f'Число {n} меньше числа {number}')
#         except Exception as error:
#             print(error, 'Нужно ввести ЧИСЛО')
#             raise
#         print(f'Список чисел меньше {n} - {answers} ')
#
#
# task_1(variable_for_task_1)

variable_for_task_4 = input('Введите переменную для задания 4 - ')


def task_4(n):
    try:
        n=int(n)
        if n != 0:
            for k in range(1, n):
                try:
                    q = (((-1) ** k) * (k - 7)) / (2 * (n - k) + 2 * (n - k))
                    print(f'Ответ - {q}')
                except Exception as error:
                    print(error)
                    raise
        else:
            print('n не может быть равно 0')
    except Exception as error:
        print(error, 'Нужно ввести ЧИСЛО')
        raise


task_4(variable_for_task_4)
