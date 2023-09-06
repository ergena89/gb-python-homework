import os
from datetime import datetime

pb_list = []
file_id = 0
# путь к выполняемому файлу (phonebook.py)
app_path = os.path.dirname(__file__)
# print(__file__, app_path)
# путь к папке с файлами с данными телефонной книги
data_dir_path = os.path.join(app_path, "data")
# print("data_dir_path:", data_dir_path)

def load_phonebook_in_ram():
    global file_id
    # цикл, по получению полных путей файлов данных и чтение этих файлов
    for filename in os.listdir(data_dir_path):
        # print(filename)
        filepath = os.path.join(data_dir_path, filename)
        # print(filepath)
        file = open(filepath, 'r', encoding='utf-8')
        for line in file:
            # print(line)
            words = line.split()
            # print(words)
            pb_rec = {
                "fam": words[0],
                "im": words[1],
                "ot": words[2],
                "number": words[3],
                "fio": words[0] + " " + words[1] + " " + words[2],
                "path": filepath,
                "id": file_id
            }
            file_id = file_id + 1
            # print(pb_rec)
            pb_list.append(pb_rec)
        file.close()
    # print(pb_list)



def find_record():
    print('Введите часть ФИО: ')
    search_string = input()
    # print (search_string)
    for pb_rec in pb_list:
        #print(pb_rec)
        if search_string.lower() in pb_rec["fio"].lower():
            print(pb_rec["id"], ")", pb_rec["fam"], pb_rec["im"], pb_rec["ot"], pb_rec["number"])
def create_record(is_new = False):
    global file_id
    if is_new:
        print('Создание новой записи!')
    else:
        print('Изменение записи!')
    pb_rec = {}
    print('Введите фамилию: ')
    inline = input().strip()
    pb_rec["fam"] = inline if inline != "" else "нет"
    print('Введите имя: ')
    inline = input().strip()
    pb_rec["im"] = inline if inline != "" else "нет"
    print('Введите отчество: ')
    inline = input().strip()
    pb_rec["ot"] = inline if inline != "" else "нет"
    print('Введите номер телефона: ')
    inline = input().strip()
    pb_rec["number"] = inline if inline != "" else "нет"

    # для сохранения на диске и в памяти нужны:
    pb_rec["fio"] =  pb_rec["fam"] + " " + pb_rec["im"] + " " + pb_rec["ot"]
    pb_rec["id"] = file_id
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
    filepath = os.path.join(data_dir_path, filename)
    pb_rec["path"] = filepath
    #print(pb_rec)
    file_id = file_id + 1
    # создать на диске
    saves_string = ' '.join([pb_rec["fam"], pb_rec["im"], pb_rec["ot"], pb_rec["number"]])
    file = open(pb_rec["path"], 'w', encoding='utf 8')
    file.writelines(saves_string)
    file.close()
    # создать в памяти
    pb_list.append(pb_rec)

def update_record():
    global file_id
    print('Введите номер записи: ')
    inline = int(input())
    for pb_rec in pb_list:
        # print(pb_rec)
        if inline == pb_rec["id"]:
            pb_list.remove(pb_rec)
            os.remove(pb_rec["path"])
            create_record()
def delete_record():
    print('Введите номер записи: ')
    inline = int(input())
    # print(inline)
    for pb_rec in pb_list:
        # print(pb_rec)
        if inline == pb_rec["id"]:
            # print(pb_rec)
            pb_list.remove(pb_rec)
            os.remove(pb_rec["path"])
            print('Запись удалена')