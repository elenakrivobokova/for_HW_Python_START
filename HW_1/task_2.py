# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

S = int(input('Введите общее количество журавликов, кратное 6: '))

if S % 6 == 0:
    x = S // 6
    print(f'Петя сделал {x} журавликов')
    print(f'Сережа сделал {x} журавликов')
    print(f'Катя сделала {4 * x} журавликов')
else:
    print('Введенное количество не кратно 6. Введите другое число')
