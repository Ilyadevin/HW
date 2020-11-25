# Задание 20
import random

a = []
q = int(input('Введите размерность квадратной матрицы - '))


def diagonal(l, c, N_2):
    multi = 1
    i = 0
    s = 0
    while i < N_2:
        if c == '1':
            multi *= l[i][i]
        else:
            s += l[i][N_2 - i - 1]
        i += 1
    return s


def launch(N_1):
    for i in range(N_1):
        w = len(i)
        b = []
        for j in range(N_1):
            n = random.randint(1, 100)
            b.append(n)
            print("%3d" % n, end='')

        a.append(b)
        print()

    ch = input("Главная (1) или побочная (2): ")
    if ch == '1' or ch == '2':
        summa = diagonal(a, ch, q)
        print(summa)


launch(N_1=q)
