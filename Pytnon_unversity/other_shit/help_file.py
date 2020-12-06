# for i in range(1, 100):
#     a = i ** 2
#     a_ = str(a)
#     a_reversed = reversed(a_)
#     if a_ == a_reversed:
#         print("hh")
#     else:
#         print("gg", type(a_))
# import random
#
# a = []
# N = int(input('Введите количество столбцов матрицы - '))
# M = int(input('Введите количество строк матрицы - '))
#
#
# def diagonal(B):
#     s = 0
#     average = 0
#     g_list = []
#     for i in B:
#         for j in i:
#             s += j
#             # print("%3d" % n, end='')
#         average = s / len(i)
#         g_list.append(average)
#         print()
#     return g_list
#
#
# def launch(N_1, M_1):
#     for i in range(N_1):
#         b = []
#         for j in range(M_1):
#             n = random.randint(1, 100)
#             b.append(n)
#             print("%3d" % n, end='')
#         a.append(b)
#         print()
#
#     average_1 = diagonal(B=a)
#     for w in average_1:
#         print("%3d" % w, end=' ')
#
#
# launch(N_1=N, M_1=M)
import random

a = []
N = int(input('Введите количество столбцов матрицы - '))


def qwerty(B):
    q = 0
    w = 0
    list_a = []
    list_b = []
    for i in B:
        if i % 2 == 0:
            list_a.append(i)
            q += 1
        else:
            list_b.append(i)
            w += 1
    print(q, w, list_b, list_a)
    return q, w, a


def launch(N_1):
    for i in range(N_1):
        n = random.randint(1, 100)
        a.append(n)
    average = qwerty(B=a)

launch(N_1=N, )
