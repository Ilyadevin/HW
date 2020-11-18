# Задание 20
import random

a = []
q = int(input('Введите размерность квадратной матрицы - '))


def diagonal(l, c, N):
    mult = 1
    i = 0
    s = 0
    while i < N:
        if c == '1':
            mult *= l[i][i]
        else:
            s += l[i][N - i - 1]
        i += 1
    return s


def launch(N):
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
        summa = diagonal(a, ch, q)
        print(summa)


launch(N=q)
