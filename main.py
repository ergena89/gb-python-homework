# n = int(input('введите число:'))
# rez = 1
# i = 1
# while i <= n:
#     rez *= i # result = result * i
#     i += 1  # i = i + 1
# print(f'{n}! = {rez}')

# фибаначи
# n = int(input('введите число:'))
# a0 = 0
# a1 = 1
# for i in range(n):
#     print(a0, end="")
#     x = a0 + a1
#     a0 = a1
#     a1 = x

# n = int(input("Введите число: "))
# a0 = 0
# a1 = 1
# x = 1
# i = 2
# while x < n:
#     x = a0 + a1
#     a0 = a1
#     a1 = x
#     i += 1
#     if x > n:
#         i = 0
        
# if i != 0:
#     print(i)
# else:
#     print(-1)

# # 15.
# n = int(input("Введите количество арбузов: "))
# x = int(input("Введите массу арбузов: "))
# min_massa, max_massa = x, x
# for i in range(n-1):
#     x = int(input("Введите массу арбуза: "))
#     if x > max_massa:
#         max_massa = x
#     elif x < min_massa:
#         min_massa = x
# print(min_massa, max_massa)

#13.
# n = int(input("Введите количество дней от 1 до 100 вкл: "))
# x = int(input("Введите среднесуточную температуру: "))
# ottepel_max = 0
# ottepel = 0
# for i in range(n-1):
#     x = int(input("Введите среднесуточную температуру:"))
#     if x > 0:
#         ottepel += 1
#         if ottepel > ottepel_max:
#               ottepel_max = ottepel
#         else:
#                 ottepel = 0
# print(ottepel_max)

# счастливый билетик
# n = 385916
# k6 = n % 10
# k5 = ((n // 10) % 10)
# k4 = ((n // 100) % 10)
# k3 = ((n // 1000) % 10)
# k2 = ((n // 10000) % 10)
# k1 = n // 100000
# l1 = (k1 + k2 + k3)
# l2 = (k4 + k5 + k6)
# if l1 == l2:
#     print('yes')
# else:
#     print('no')

# # Определите, можно ли от шоколадки размером a × b долек отломить c долек, 
# # если разрешается сделать один разлом по прямой между дольками 
# # (то есть разломить шоколадку на два прямоугольника).
# # Выведите yes или no соответственно.
# # Пример:
# # a, b, c = 3, 2, 4 -> yes
# # a, b, c = 3, 2, 1 -> no

a = 1
b = 1
c = 1
# if (a % c == 0 and c <= a * b) or (b % c == 0 and c <= a * b):
#     print('yes')
# else:
#     print('no')

# if c <= b * a and (c % a == 0 or c % b == 0):
#     print('yes')
# else:
#     print('no')