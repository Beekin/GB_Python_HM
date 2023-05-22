# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите длину: "))
m = int(input("Введите ширину: "))
k = int(input("Кол-во долек: "))

if k == m or k == n:
    
    print(f'{n} {m} {k} -> Yes')

elif (m*n) % 2 == 0 and k % 2 == 0 and k < (m*n):

    print (f'{n} {m} {k} -> Yes')

elif (m*n) - k == n or (m*n) - k == m:

    print (f'{n} {m} {k} -> Yes')

elif k < (m*n) and k % m == 0 or k % n == 0 :

    print (f'{n} {m} {k} -> Yes')

else:

    print (f'{n} {m} {k} -> No')
