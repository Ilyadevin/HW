# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 08:34:56 2020

@author: student
"""

print('I', 'like', 'Python', sep=' ')
print()
my_range = 5
a = '*'
print(a)

for _ in range(5):
    a += '*'
    print(a)

print()

i = 0
b = '*'
print(b)
while i != my_range:
    i += 1
    b += '*'
    print(b)
else:
    pass

print()

print('Введите значения H и L')
h = input()
l = input()
while type(h) and type(l) != float:
    try:
        h = float(h)
        l = float(l)
    except ValueError:
        print('Введите корректные значения H и L')
        h = input()
        l = input()
print("Результат %e" % (h * l))
print("Результат %0.2f" % (h * l))
print("Результат {:.0e}".format(h * l))
print("Результат {:.1e}".format(h * l))
print("Результат {:10.2f}".format(h * l))
print("{:,.2f}".format(h * l))

print()

list_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Division_1 = []
Division_2 = []
first_division = 0
second_division = 0
for i in list_1:
    for j in list_2:
        first_division = i // j
        second_division = i % j
    Division_1.append(first_division)
    Division_2.append(second_division)

print(f'Целочисленное деление - {Division_1}')

print()

print(f'Деление с остатком - {Division_2}')

print()

print('Преобразование типов ')

print()

list_types = ['1995', 1.94, '98.36', 'Привет']
for i in list_types:
    try:
        print(type(str(i)), str(i))
        print()
        print(type(int(i)), int(i))
        print()
        print(type(float(i)), float(i))
        print()
    except Exception as error:
        print(error)

