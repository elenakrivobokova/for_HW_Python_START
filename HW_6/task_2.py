# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random

arr = [random.randint(-20, 20) for i in range(1,20)]
print(arr)
range_1 = (int(input('Задайте нижнюю границу диапазона: ')))
range_2= (int(input('Задайте верхнюю границу диапазона: ')))
arr_new = []
for i, val in enumerate(arr, start=0):  
    if range_1 < val < range_2:
        arr_new.append(i)
print(arr_new)


# arr_new = [arr_new.append(i) for i, val in enumerate (arr, start=0) if range_1 < val < range_2]
# print(arr_new)



