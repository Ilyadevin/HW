from random import randint

dict_ = {}


def generating_dict():
    for i in range(1, 10):
        dict_[i] = randint(1, 10)
    return dict_


def sum_values():
    summ = 0
    for i in dict_.values():
        summ += i
    return summ


def summ_keys():
    summ = 0
    for i in dict_.keys():
        summ += i
    return summ


generated_dict, values_summ, keys_summ = generating_dict(), sum_values(), summ_keys()
print(f'{generated_dict} - сгенерированный словарь')
if values_summ > keys_summ:
    print('Сумма значений больше ключей')
    print(f'{values_summ} > {keys_summ}')
elif values_summ < keys_summ:
    print('Сумма ключей больше значений')
    print(f'{values_summ} < {keys_summ}')
else:
    print('Сумма ключей равна значений')
    print(f'{values_summ} = {keys_summ}')
