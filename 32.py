# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно
# На входе : [ 1, 5, 88, 100, 2, -4]
from random import randint as rd
n = int(input("Введите кол-во элементов списка n: "))
list_1 = list()
for i in range(n):
        list_1.append(rd(0, 100))
print(list_1)
start = int(input("Введите начало диапазона start: "))
stop = int(input("Введите конец диапазона stop: "))
list_res = list()
for i in range(n):
        if list_1[i] >= start and list_1[i] <= stop:
                list_res.append(i)
print(list_res)
