numbers = [0.6, 15.65, 79.87, 45.6, 3.9]


def round_numbers(nums):
    for q in range(len(nums)):
        nums[q] = round(nums[q])
    print(f'Список с округленными числами - {nums}')
    return nums


def maximum():
    list_num = round_numbers(nums=numbers)
    maximum_par = 0
    for i in list_num:
        if i > maximum_par:
            maximum_par = i
        else:
            pass
    return maximum_par


print(f'Ответ - {maximum()}')
