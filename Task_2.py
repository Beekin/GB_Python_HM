# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

a = int(input("Введите число: "))

sum = 0

while a > 9:

    sum += a % 10 
    
    a = a // 10

sum = sum + a
     
print (f'Сумма цифр = {sum}')

