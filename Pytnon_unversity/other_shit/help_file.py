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
# import random
#
# a = []
# N = int(input('Введите количество столбцов матрицы - '))
#
#
# def qwerty(B):
#     q = 0
#     w = 0
#     list_a = []
#     list_b = []
#     for i in B:
#         if i % 2 == 0:
#             list_a.append(i)
#             q += 1
#         else:
#             list_b.append(i)
#             w += 1
#     print(q, w, list_b, list_a)
#     return q, w, a
#
#
# def launch(N_1):
#     for i in range(N_1):
#         n = random.randint(1, 100)
#         a.append(n)
#     average = qwerty(B=a)
#
# launch(N_1=N, )
Q = int(input(' -  '))
R = int(input('R - '))
W = int(input('W - '))
X = int(input('X - '))


def control(dictionary):
    print(dictionary)
    counter_R = 0
    counter_W = 0
    counter_X = 0
    for q in dictionary.values():
        for w in q:
            command = input('Выберите комманду - X R W ')
            if command == 'R':
                counter_R += 1
                if w == command:
                    if 'R' in q:
                        if q['R'] != counter_R:
                            print('OK')
                        else:
                            print('Access denied')
                    else:
                        print('Access denied')
                else:
                    print('Access denied')
            elif command == 'W':
                counter_W += 1
                if w == command:
                    if 'W' in q.keys():
                        if q['W'] != counter_W:
                            print('OK')
                        else:
                            print('Access denied')
                    else:
                        print('Access denied')
                else:
                    print('Access denied')
            elif command == 'X':
                counter_X += 1
                if w == command:
                    if 'X' in q.keys():
                        if q['X'] != counter_X:
                            print('OK')
                        else:
                            print('Access denied')
                    else:
                        print('Access denied')
                else:
                    print('Access denied')
            else:
                print('Неверная комманда')


def filling_dict(N):
    dict_ = dict()
    for i in range(N + 1):
        if i % 2 == 0:
            dict_[N] = {i: [R, W]},
            dict_[i] = {'R': R, 'W': W}
        elif i % 3 == 0:
            dict_[N] = {i: [X, W]}
            dict_[i] = {'X': X, 'W': W}
        else:
            dict_[N] = {i: [R, W, X]},
            dict_[i] = {'X': X, 'W': W, 'R': R}
    return dict_


control(dictionary=filling_dict(Q))
