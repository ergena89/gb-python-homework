# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите кол-во элементов n: "))
m = int(input("Введите кол-во элементов m: "))
list_1 = list()
list_2 = list()
for i in range(n):
    list_1.append(input("Введите число для n: "))
for j in range(m):
    list_2.append(input("Введите число для m: "))
# print(list_1)
# print(list_2)
set1 = set(list_1 + list_2)
list3 = list(set1)
list3.sort(reverse = False)
print(list3)
