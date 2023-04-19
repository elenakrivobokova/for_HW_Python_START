# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import random
N = int(input('Введите количество элементов в массиве: '))
lst = [random.randint(1, 5) for i in range(N)] # print(list(range(1, N+1)))
print(lst)
x = int(input('Введите натуральное число для сравнения: '))
print(x)

ind = 0
min = abs(x - lst[0])
for i in range(2, N):
    dif = abs(x - lst[i])
    if dif < min:
        min = dif
        ind = i
print(lst[ind])

