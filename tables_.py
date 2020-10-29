import math

h = 0.25
i = -3
el_list = list()
sum_1 = 0  # Сумма по первому условию
sum_2 = 0  # Сумма по второму условию
while i <= 2:
    if i > 0:
        for k in range(1, 5):
            el_list.append(i ** k)
    if i <= 0:
        sum_2 = math.pi ** (3.5 * i)
    i += h
    print(f'Выполнение условия - x<= 0 - {sum_2}')
else:
    print('Выход из цикла.')
for i in el_list:
    sum_1 += i
print(f'Сумма при выполнении условия x>0 - {sum_1}')
print('Выход из программы.')
