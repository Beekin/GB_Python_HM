#  Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

a = int(input("Введите количество поделок: "))

if a % 3 == 0:

    b = a // 3

    print (f'Катя сделала: {b*2}, а Петя и Сережа сделали по {b // 2}')

elif a % 3 == 0 & a < 9 & a != 6:

        b = a // 3

        print (f'Катя сделала: {b*2 + 1}, а Петя и Сережа сделали по {b // 2}')

elif a % 2 == 0:

    b = a // 2

    if b % 2 == 0:

        print (f'Катя сделала: {b}, а Петя и Сережа сделали по {b // 2}')

    elif b % 2 != 0:

        print (f'Катя сделала: {b + 1}, а Петя и Сережа сделали по {b // 2}')   

elif a % 2 !=0:

    print ("Не подходит под условие задачи")



