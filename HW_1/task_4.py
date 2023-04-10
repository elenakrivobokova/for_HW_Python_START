# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

n = int(input('Введите длину шоколадки: '))
m = int(input('Введите ширину шоколадки: '))
k = int(input('Введите количество долек шоколадки: '))
if n <= 0 or m <= 0 or k <= 0:
    print('Введенные числа должны быть положительными')
else:
    if (k % n == 0 or k % m == 0) and k < n * m:
        print(f'Шоколадку ПОЛУЧИТСЯ разломить на два прямоугольника')
    else:
        print(f'Шоколадку НЕ ПОЛУЧИТСЯ разломить на два прямоугольника')
