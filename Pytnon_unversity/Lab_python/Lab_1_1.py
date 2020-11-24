a = int(input('Значение a - '))
b = int(input('Значение b - '))
c = int(input('Значение c - '))
k = int(input('Значение k - '))
d = int(input('Значение d - '))
try:
    result = (((a ** 2) - (b ** 3) - (c ** 3) * (a ** 2)) * (b - c + c * (k - d / (b ** 3))) - (((k / b - k / a) * c)) ** 2) - 20000
    print(result)
except Exception as error:
    print(error)
    print('Введите правильные данные! ')