from phonebook import find_record, create_record, update_record, delete_record, load_phonebook_in_ram

print('Загружаю справочник с диска в оперативную память')
load_phonebook_in_ram()
print('Здравствуйте')
print('Вы находитесь  в меню справочника')

while True:
    print()
    print('1 - найти запись\n'
          '2 - новая запись\n'
          '3 - редактирование записи\n'
          '4 - удаление записи\n'
          '5 - Выйти из программы\n')
    command = int(input('Введите номер команды(1-5): '))
    if command not in [1, 2, 3, 4, 5]:
        print('Ошибочный запрос')
    elif command == 1:
        find_record()
    elif command == 2:
        create_record(True)
    elif command == 3:
        update_record()
    elif command == 4:
        delete_record()
    elif command == 5:
        print('Всего доброго!')
        break