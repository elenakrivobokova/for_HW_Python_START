# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


def exp(a, b):
   if b == 0:
      return 1
   return a * exp(a, b - 1)
    
num_1= int(input('Введите число A: '))
num_2 = int(input('Введите число B: '))
print(exp(num_1, num_2))


# 2й вариант

# power = lambda a, b: a * power(a, b - 1) if b else 1

# print(power(2, 4))
