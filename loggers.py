from loggers import  find_data
def find_data():
    print('Введите номер файла: ')
    file_name = input()
    data = open(fale_name+'.txt', 'r', encoding='utf-8')
    for line in data:
        print(line)
    data.close()
find_data()

def new_data():
    print('Введите название нового файла: ')
    new_number = str(input())
    data = open(new_file_name+'.txt', 'w', encoding='utf-8')
    print('Введите ФИО и номер телефона (+7...) через пробел: ')
    original_data = input()
    data.write(original_data)
    data.close()

def correction_data():
    print('Введите имя файла: ')
    file_name = input()
    data = open('file_name+.txt', 'w', encoding= 'utf 8')
    print(data.read())
    data.close()

    data = open('file_name+.txt', 'w', encoding= 'utf 8')
    print('Введите НОВЫЕ! ФИО и номер телефона(+7) через пробел: ')
    original_data = input()
    data.write(original_data)
    data.close()