# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# list_1 = [1, 2, 3, 4, 3]
# k = 3
# cnt = 0
# for elem in list_1:
# 	if elem == k:
# 		cnt += 1
# print(cnt)

# 18. Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
# list_1 = [1, 2, 3, 4, 5, 5]
# k = 6
# rez = 0
# for i in range(len(list_1)):
#     if k - list_1[i] == 0:
#         rez = list_1[i]
#         print(rez)
# for i in range(len(list_1)):
#     if rez != 0:
#         break
#     elif k - list_1[i] == 1 or k - list_1[i] == -1:
#         rez = list_1[i]
#         print(rez)

# вариант от преподавателя
# n = int(input("Введите кол-во элементов списка: "))
# data_list = list()
# for i in range(n):
#     data_list.append(rd(1, 10))
# print(data_list)
# x = int(input("Введите число x: "))
# min_diff = abs(x - data_list[0])
# result_number = data_list[0]
# for i in range(1, n):
#     if abs(data_list[0] - x) < min diff:
#         mindiff = abs(data_list[i] - x)
#         result_number = data_list[i]
# print(f"Максимально приближенное число из списка к {x} равно {result_number}")


# 20. Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# k = 'ноутбук'
# word = k.upper()
# s = 0
# list1 = [
# [["A", "E", "I", "O", "U", "L", "N", "S", "T", "R", "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"], 1], 
# [["D", "G", "Д", "К", "Л", "М", "П", "У"], 2], 
# [["B", "C", "M", "P", "Б", "Г", "Ё", "Ь", "Я"], 3], 
# [["F", "H", "V", "W", "Y", "Й", "Ы"], 4], 
# [["K", "Ж", "З", "Х", "Ц", "Ч"], 5], 
# [["J", "X", "Ш", "Э", "Ю"], 8], 
# [["Q", "Z", "Ф", "Щ", "Ъ"], 10]
# ]

# for letter in word:
#     for row in list1:
#         bukvi = row[0]
#         cenaBukvi = row[1]
#         if letter in bukvi:
#             cost = cenaBukvi
#             s += cost
#             break
#         else:
#             cost = 0
        
# print(s)

# вариант от Димы
# word = "hello"
# word = word.upper()
# k = 0

# list1 = [
# [["A", "E", "I", "O", "U", "L", "N", "S", "T", "R", "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"], 1], 
# [["D", "G", "Д", "К", "Л", "М", "П", "У"], 2], 
# [["B", "C", "M", "P", "Б", "Г", "Ё", "Ь", "Я"], 3], 
# [["F", "H", "V", "W", "Y", "Й", "Ы"], 4], 
# [["K", "Ж", "З", "Х", "Ц", "Ч"], 5], 
# [["J", "X", "Ш", "Э", "Ю"], 8], 
# [["Q", "Z", "Ф", "Щ", "Ъ"], 10]
# ]
# for letter in word:
#     #print(letter)
#     for row in list1:
#         #print(row)
#         bukvi = row[0]
#         cenaBukvi = row[1]
#         #print(bukvi, cenaBukvi)
#         if letter in bukvi:
#             cost = cenaBukvi
#             break
#         else:
#             cost = 0
#     print(letter, cost)
#     # if letter in thisdict:
#     #     cost = thisdict[letter]
#     # else:
#     #     cost = 0
#     # print(letter, cost)
#     k += cost
# print('Word Points: ',k)

# вариант от преподавателя
# points = {"A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т": 1, и тд...}
# # .lower() <-> .upper()
# word = input("Введите текст: ").upper()
# count = 0
# for char in word:
#     for key in points:
#         if char in key:
#             count += points[key]
# print(count)


