# Задание 20
# import random
# list_a = []
# data = random.randint(1, 100)
# # print(data, 'debug 2')
# result = list()
# mult = 1
# N_strings = input('Число строк - ')
# N_Colons = input('Число столбцов - ')
# try:
#     N_strings = int(N_strings)
#     N_Colons = int(N_Colons)
# except Exception as error:
#     print(error, ' - неверный формат ввода')
# for i in range(0, int(N_Colons)):
#     list_a.append([])
#     for j in range(0, int(N_strings)):
#         list_a[i].append(data)
#         mult *= list_a[i][j]
#         data = random.randint(1, 100)
#         # print(mult, 'mult debug', data, 'data debug')
#     result.append(mult)
#     # print(result, 'result debug 1')
#     mult = 1
# # print(result, 'result debug')
# for i in range(len(result)):
#     print(f'Произведение элементов исходного массива столбца {i} = {result[i]}')
import random


def diagonal(l, c):
    mult = 1
    i = 0
    while i < N:
        if c == '1':
            mult *= l[i][i]
        else:
            s += l[i][N - i - 1]
        i += 1
    return s


N = 10
a = []
for i in range(N):
    b = []
    for j in range(N):
        n = random.randint(1, 100)
        b.append(n)
        print("%3d" % n, end='')
    a.append(b)
    print()

ch = input("Главная (1) или побочная (2): ")
if ch == '1' or ch == '2':
    summa = diagonal(a, ch)
    print(summa)
