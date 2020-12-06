input_string = input('Введите строку - ')


def string_func(par):
    for i in par:
        print(f'Длина слова {i} - {len(i)}')


string_func(input_string.split(' '))
