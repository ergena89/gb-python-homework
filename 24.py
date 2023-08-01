# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
# причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное 
# число ягод — на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
from random import randint as rd
n = int(input("Введите кол-во кустов n: "))
yagodi = list()
for i in range(n):
        yagodi.append(rd(0, 20))
print(yagodi)
max_sum = 0
for i in range(n):
     sum = yagodi[(i - 1 + n) % n] + yagodi[i] + yagodi[(i + 1) % n]
     if max_sum < sum:
         max_sum = sum
print(max_sum)

