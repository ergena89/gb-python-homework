tele01 = ['Иванов', 'Василий', 'Петрович', '+79991000001']
tele01 = ' '.join(tele01)
data = open('data01.txt', 'w', encoding= 'utf 8')
data.writelines(tele01)
data.close()

tele02 = ['Васильченко', 'Евгений', 'Михайлович', '+79991000002']
tele02 = ' '.join(tele02)
data = open('data02.txt', 'w', encoding= 'utf 8')
data.writelines(tele02)
data.close()

tele03 = ['Иванова', 'Клара', 'Васильевна', '+79991000003']
tele03 = ' '.join(tele03)
data = open('data03.txt', 'w', encoding= 'utf 8')
data.writelines(tele03)
data.close()

from loggers import find_data, new_data, correction_data
def interface():
    print('Здравствуйте')
    print('Вы находитесь  в меню справочника')
    print('1 - найти запись\n'
          '2 - новая запись\n'
          '3 - редактирование записи\n'
          '4 - удаление записи\n'
          '5 - Выйти из программы\n')
    while True:
        comand = int(input('Введите номер команды(1-4): '))
        if comand not in [1, 2, 3, 4]:
            print('Ошибочный запрос')
        elif comand == 1:
            find_data()
        elif comand == 2:
            new_data()
        elif comand == 2:
            correction_data()

        elif comand == 5:
            print('Всего доброго!')
            return
if __name__ == '__main__':
    interface()