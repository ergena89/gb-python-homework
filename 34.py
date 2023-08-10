# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
def AreAllElementsEqual(arr):
    res = True
    firstElem = arr[0]
    for i in arr:
        if firstElem != i:
            res = False
            break
    return res
str = input("Введите стихотворение: ")
words = str.split()
letter_count = []
print(words)
for word in words:
     print(word)
     filter_result = list(filter(lambda letter: letter == 'а', word))
     print(filter_result)
     print(len(filter_result))
     letter_count.append(len(filter_result))
print(letter_count)

if len(letter_count) == 0:
    print('Не введено стихотворение')
else:
    if AreAllElementsEqual(letter_count):
        if letter_count[0] == 0:
            print('Пам парам, т.к. нет букв А')
        else:
            print('Парам пам-пам')
    else:
        print('Пам парам')

# print(words)
# for word in words:
#     print(word)
#     cnt = 0
#     for letter in word:
#         #print(letter)
#         if letter == 'а':
#             cnt = cnt + 1
#     print(cnt)
#     letter_count.append(cnt)