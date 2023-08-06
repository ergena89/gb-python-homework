# Array - массив
# List - список
# int[] array = new int[5]; // array = {0, 0, 0, 0, 0}
# list_1 = list()
# list_2 = [56, 12.75, -1, True, "Hello, world!"]
# set_1 = set()
# data - dict()
# data_1 = {}
# 5 - int
# "5" - str
# True - bool

# чтобы пользоваться рандомом, эту функцию необходимо сперва импортнуть к себе, а потом только использовать
# import random
# from random import randint as rd # alias (псевдоним для названия функции)
# print(randint(1, 10))

# # Дан список чисел. Определите, сколько в нем встречается различных чисел. 
# # Пользователь может вводить значения списка или список задан изначально.
# from random import randint as rd
# n = int(input("Введите кол-во элементов списка: "))
# data_list = list()
# for i in range(n):
#     data_list.append(rd(-5, 5))
# print(data_list)
# print(f'количество уникальных элементов списка', len(set(data_list)))


# # Задача № 19. Дана последовательность из N целых и число K. 
# # Необходимо сдвинуть всю последовательность (сдвиг циклический) на K элементов вправо, K - положительное число.
# from random import randint as rd
# n = int(input("Введите кол-во элементов списка: "))
# k = int(input("Введите k - число на которое необходимо сдвинуть всю последовательность: "))
# list_1 = list()
# for i in range(n):
#     list_1.append(rd(1, 10))
# print(list_1)
# list_2 = []
# k = k % n
# for i in range(n - k + 1):
#     list_2.append(list_1[i + k - 1])
# print(list_2)
# for i in range(n - k - i):
#     list_2.append(list_1[i])
# print(list_2)

# # Задача №21. Напишите программу для печати всех уникальных значений в словаре.
# data = [{"V": "S001"},{"V": "S002"},{"VI": "S001"},{"VI": "S005"},{"VII": "S005"},{"V": "S009"},{"VIII": "S007"}]
# result = set()
# for i in data:
#     for key in i:
#         result.add(i[key])
# print(result)

# Задача №23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, 
# больших предыдущего(элемента с предыдущим номером).

# from random import randint as rd
# n = int(input("Введите количество элементов: "))
# data_list = list()
# for i in range(n):
#     data_list.append(rd(-10, 10))
# print(data_list)
# rez = 0
# for i in range(n - 1):
#     if data_list[i + 1] > data_list[i]:
#         rez += 1
#         print(f'{data_list[i + 1]} > {data_list[i]}')
# print(rez)

#Семинар 4.
# # 25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# # Количество повторов добавляется к символам с помощью постфикса формата _n. Используйте функцию .split()
# input: a a a b c a a d c d d
# output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# text = input("Введите текст: ").split()
# count_char = {}
# for char in text:
#     if char not in count_char:
#         print(char, end=" ")
#         count_char[char] = 1
#     else:
#         print(f"{char}_{count_char[char]}", end=" ")
#         count_char[char] += 1
# print(text)


# 27. Пользователь вводит текст (строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним пробелом. 
# Определите, сколько различных слов содержится в этом тексте.
# text = input("Введите текст: ").lower().split()
# print(len(text))
# 2 вариант:
# print(len(set(input("Введите текст: ").lower().split())))

# 29. Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего элемента последовательности, 
# которая завешается первым встретившимся 0 (ноль не входит в последовательность). чей код ближе к правильному решению.
n = int(input('Введите число n:'))
max_number = n
    if n > max_number:
        max_number = n
print(max_number)