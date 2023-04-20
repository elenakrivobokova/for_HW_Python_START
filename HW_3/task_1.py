# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1


import random
N = int(input('Введите количество элементов в массиве: '))
lst = [random.randint(0, 10) for i in range(N)]
print(lst)
x = int(input('Введите искомый элемент: '))
print(x)

# x = lst.count(x) # I ВАРИАНТ
# print(x)

# my_lst = [x == i for i in lst] # II ВАРИАНТ
# print(sum(my_lst))
# my_lst = [x == i for i in lst] # III ВАРИАНТ
# print(sum(my_lst))

# IV ВАРИАНТ
lst_1 = []
ind = 0
for i in lst:
    if x == lst[ind]:
        lst_1.append(x)
        ind += 1
    else: ind += 1

print(lst_1)
print(len(lst_1))
