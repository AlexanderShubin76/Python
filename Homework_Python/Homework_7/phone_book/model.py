# Модуль отвечает за внутреннюю логику программы. Здесь хранятся методы для добавления, удаления, перезаписи
# id в телефонном справочнике. Также созданы методы для экспорта телефонной книге в форматы .csv или .txt.
# Справочник хранится в файле "phone_book.p". Справочник включает следующие поля : id, ФИО, день рождения,
# место работы, номер. 
import pickle
# phone_book = {
#     '1': {'ФИО': 'Иванов И.П', 'День рождения': '15.03.02', \
#         'Место работы': 'ОАО "Газпром"', 'Номер телефона': {'личный' : '123'}},
#     '2': {'ФИО': 'Петров И.Г', 'День рождения': '16.04.92', \
#         'Место работы': 'ОАО "Роснефть"', 'Номер телефона': {'рабочий' : '333', 'личный' : '789'}},
#     '3':   {'ФИО': 'Крючкова Т.П', 'День рождения': '22.11.93', \
#         'Место работы': 'ОАО "Сбербанк"', 'Номер телефона': {'личный' : '788'}},
#     '4': {'ФИО': 'Васечкин А.В.', 'День рождения': '27.02.91', \
#         'Место работы': 'ОАО "Ригла"', 'Номер телефона': {'рабочий' : '781', 'личный' : '111'}},
#     '5': {'ФИО': 'Потехин А.В.', 'День рождения': '21.10.95', \
#         'Место работы': "Мосводоканал", 'Номер телефона': {'личный' : '055'}},
# }
# Извлекаем наш измененный при предыдущих запусках программы словарь из файла с расширением .pickle

phone_book = pickle.load(open( "phone_book.p", "rb" ) ) 

# Метод добавления или изменения записи в телефонном справочнике
def add_id(id, FIO, birth_date, work_place, tel_number_personal, tel_number_working): 
    phone_book[id] = {'ФИО': FIO, 'День рождения': birth_date, \
        'Место работы': work_place, 'Номер телефона': {'личный': tel_number_personal, 'рабочий': tel_number_working}}
     #Чтобы изменения сохранились, добавляем словарь с изменениями в файл с расширением .pickle
    pickle.dump(phone_book, open("phone_book.p", "wb")) 



def del_id(id): # Метод удаления записи из телефонного справочника
    del phone_book[id]
    pickle.dump(phone_book, open("phone_book.p","wb" ))


def export_txt_format(file): # Экспортируем данные из телефонной книги в файл формата .txt
        with open(file, 'w') as file:
            for line in phone_book.items():
                file.write(str(line) + '\n')


def export_csv_format(file): # Экспортируем данные из телефонной книги в файл формата .csv

    with open(file, 'w') as file_1:
        file_1.write('id; FIO; birth_date; work_place; tel_number_personal; tel_number_working\n')
        for i,r in phone_book.items():
            id = i
            FIO = r['ФИО']
            birth_date = r['День рождения']
            work_place = r['Место работы']
            if 'личный' in r['Номер телефона']:
                tel_number_personal = r['Номер телефона']['личный']
            else:
                tel_number_personal = '-'
            if 'рабочий' in r['Номер телефона']:
                 tel_number_working = r['Номер телефона']['рабочий']
            else:
                tel_number_working = '-'
           
            file_1.write(f'{id}; {FIO}; {birth_date}; {work_place}; {tel_number_personal}; {tel_number_working}\n')
            # print(f'{id}; {FIO}; {birth_date}; {work_place}; {tel_number_personal}; {tel_number_working}\n')







