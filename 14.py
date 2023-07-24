# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N
n = int(input("Введите число n: "))
for i in range(n):
    power = pow(2, i)
    if power <= n:
        print(power)
    else:
        break