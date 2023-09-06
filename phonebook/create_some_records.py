tele01 = ['Иванов', 'Василий', 'Петрович', '+79991000001']
tele01 = ' '.join(tele01)
data = open('data/data01.txt', 'w', encoding='utf 8')
data.writelines(tele01)
data.close()

tele02 = ['Васильченко', 'Евгений', 'Михайлович', '+79991000002']
tele02 = ' '.join(tele02)
data = open('data/data02.txt', 'w', encoding='utf 8')
data.writelines(tele02)
data.close()

tele03 = ['Иванова', 'Клара', 'Васильевна', '+79991000003']
tele03 = ' '.join(tele03)
data = open('data/data03.txt', 'w', encoding='utf 8')
data.writelines(tele03)
data.close()