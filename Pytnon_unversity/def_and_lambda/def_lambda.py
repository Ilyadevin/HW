# list_of_numbers_m = [1, 2, 3, 4, 99, 88, 77, 45, 87, 66, 55, 34, 88, 99, 44, 6655, 9988]
#
#
# def sum_and_average(m):
#     summ = 0
#     n = len(m)
#     for i in m:
        summ += i
    average = summ / n
    return average


print(f'Среднее арифметическое массива - {round(sum_and_average(list_of_numbers_m), 2)}')
from random import randint


def list_appear(N):
    a = []
    for i in range(N):
        a.append(randint(1, 99))
    print(f'Массив до сортировки методом пузырька - {a}')
    return a


def sorting(a_to_sort):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a_to_sort[j] > a_to_sort[j + 1]:
                a_to_sort[j], a_to_sort[j + 1] = a_to_sort[j + 1], a_to_sort[j]
    return a_to_sort


N = int(input('Введите размерность списка - '))

print(f'Массив после сортировки методом пузырька - {sorting(list_appear(N))}')
import math

x = int(input('Введите x - '))


def sh_1(x):
    sh = (math.e ** x - math.e ** (-x)) / 2
    return sh


def sh_2():
    sinh = math.sinh(sh_1(x)) * math.tan(x + 1)
    return sinh


def sh_3():
    sinh_3 = math.sqrt(1 - math.sin(2 + sh_1(x - 1)))
    return sinh_3


print(sh_2() - sh_3())
from random import randint

numbers = []
for i in range(15):
    numbers[i] = randint(1, 100)
    
