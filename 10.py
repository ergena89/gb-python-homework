# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
n = int(input("Введите количество монеток n: "))
monet_reshka = 0
monet_gerb = 0
for i in range(n):
    x = int(input(f"Введите сторону монеты {i+1}(если герб, введите - 1, если reshka, введите - 2):"))
    if x == 2:
        monet_reshka +=1
    else: 
        x == 1
        monet_gerb += 1
if monet_gerb <= monet_reshka:
    print(f'необходимо перевернуть {monet_gerb} монет')
else:
    print(f'необходимо перевернуть {monet_reshka} монет')