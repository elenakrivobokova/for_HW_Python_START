# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

I ВАРИАНТ
import random
N = int(input('Введите натуральное число: '))
lst = [random.randint(0, 1) for i in range(N)]
print(lst)
x = random.randint(0, 1)
print(x)
x = lst.count(x)
print(x)

# II ВАРИАНТ
# import random
# N = int(input('Введите натуральное число: '))
# lst = [random.randint(0, 1) for i in range(N)]
# print(lst)
# x = random.randint(0, 1)
# print(x)
# lst_1 = []
# num = 0
# for i in lst:
#     if x == lst[num]:
#         lst_1.append(x)
#         num += 1
#     elif x != lst[num]:
#         num +=1

# print(lst_1)
# print(len(lst_1))
