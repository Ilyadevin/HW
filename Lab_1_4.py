new_index = input("Введите исла через запятую - ")
list_ints = new_index.split(', ')
count_i = 0
sum_ = 0
for i in list_ints:
    sum_ = sum_ + int(i)
    count_i += 1
print(f"Среднее арифметическое - {sum_/count_i}")
