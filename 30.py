a1 = int(input("Введите первый элемент прогрессии a: "))
razn = int(input("Введите разность n - 1: "))
d = int(input("Введите кол-во элементов прогрессии d: "))
list_1 = [d]
for i in range(d):
    k = a1 + razn*d
    list_1.append(k)
    a1 = k
print(list_1)
