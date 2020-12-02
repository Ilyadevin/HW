# def recursive(input_par):
#     right_array = list()
#     for q in range(len(input_par)):
#         i = 0
#         if input_par[q] == ' ':
#             i += 1
#             if input_par[q + 1] == ' ' and i >= 1:
#                 # print(i)
#                 right_array.append(input_par[q])
#                 print(right_array)
#                 input_par.replace(input_par[q + 1], '', 1)
#         elif input_par[q] == ',':
#             if input_par[q + 1] == ' ':
#                 input_par.replace(input_par[q + 1], '', 1)
#         elif input_par[q] == ',':
#             if input_par[q + 1] == ' ':
#                 input_par.replace(input_par[q + 1], '', 1)
#         reversed_array = q * (-1)
#         c = ''
#         c.join()
#         # print(reversed_array)
#         # print(input_par)
#
#
# recursive('ss  qaw  1,  23')
from random import randint


def Smooth(A, N):
    Q = 0
    while Q < 5:
        for i in range(1, N - 1):
            A[0] = round((A[0] + A[1]) / 2, 2)
            A[-1] = round((A[-1] + A[-2]) / 2, 2)
            A[i] = round((A[i - 1] + A[i + 1]) / 2)
        print(f'Результаты выполнения сглаживания - {A}, порядка - {Q+1}')
        Q += 1


N = int(input('Введите размер списка - '))
A = []

for i in range(N):
    A.append(randint(0, 1000))
Smooth(A, len(A))
