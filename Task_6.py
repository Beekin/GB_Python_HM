# Задача 6:Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

a = int(input("Введите 6-ти значный номер билета: "))

s1 = 0
s2 = 0

if a < 99999 or a > 999999:   
    
    print("Введенный номер неверный ")

else:
    d = a

    while d > 999:

        c = d % 10 

        s1 += c % 10

        d = d // 10

      

    f = a // 1000

    while f > 0:

        c = f % 10 

        s2 += c % 10

        f = f // 10
 

    if s1 == s2:

        print(f"{a} -> счастливый билет")

    else:

        print(f"{a} -> несчастливый билет")