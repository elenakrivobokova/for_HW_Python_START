# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

num = str(input('Введите номер из шести цифр: '))
if len(num) == 6:
    num = int(num) 
    sum1 = 0 
    while num // 1000 > 0:
        sum1 = sum1 + num % 10 # + (num // 10) % 10 + (num // 100) % 10 
        num //= 10
    else:
        sum2 = num % 10 + num // 10 % 10 + num // 100
    if sum1 == sum2:
        print('Поздравляем! У Вас счастливый билетик!')
    else: 
        print('К сожалению, билетик не является счастливым!') 
else:
    print('Номер не шестизначный. Попробуйте еще раз!')
