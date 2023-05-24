# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке.

# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод:
# Парам пам-пам

def poem(x):
    str_1 = x.split()
    print(str_1)
    str_2 = []
    for i in str_1: 
        sum = 0
        vowels = set('аеёиоуыэюя')   
        for letter in i:
            if letter in vowels:
                sum += 1
        str_2.append(sum)
    if len(set(str_2)) == 1:
        print('Парам пам-пам')
    else:
        print('Пам парам')
my_text = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
poem(my_text)



    
