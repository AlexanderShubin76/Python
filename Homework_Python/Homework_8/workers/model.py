# Модуль отвечает за внутреннюю логику программы. 
# Здесь хранятся 3 группы методов.
# 1-я группа методов представлена методами для добавления, удаления, обновления данных о сотруднике.
# 2-я группа методов необходима для экспорта данных о сотрудниках в форматы .csv или .json.
# Данные о сотрудниках хранятся в файле "workers.p". Данные о сотрудниках включает следующие поля:
# id, last_name, first_name, post, tel_number, salary.
import pickle
import json

workers = {
    '1': {'last_name': 'Иванов', 'first_name': 'Иван', 'post': 'Инженер-химик', \
        'tel_number': '878', 'salary': 95000},
    '2': {'last_name': 'Петров', 'first_name': 'Сергей', 'post': 'Электрик', \
        'tel_number': '578', 'salary': 60000},
    '3': {'last_name': 'Васильев', 'first_name': 'Александр', 'post': 'Водитель', \
        'tel_number': '222', 'salary': 62000},
    '4': {'last_name': 'Иванов', 'first_name': 'Иван', 'post': 'Инженер', \
        'tel_number': '878', 'salary': 95000},
    '5': {'last_name': 'Иванов', 'first_name': 'Иван', 'post': 'Инженер', \
        'tel_number': '878', 'salary': 95000},
}
# Извлекаем наш измененный при предыдущих запусках программы словарь из файла с расширением .pickle
pickle.dump(workers, open("workers.p","wb" ))
workers = pickle.load(open( "workers.p", "rb" ) ) 

# Метод добавления или изменения записи в телефонном справочнике
def add_id(id, FIO, birth_date, work_place, tel_number_personal, tel_number_working): 
    workers[id] = {'ФИО': FIO, 'День рождения': birth_date, \
        'Место работы': work_place, 'Номер телефона': {'личный': tel_number_personal, 'рабочий': tel_number_working}}
     #Чтобы изменения сохранились, добавляем словарь с изменениями в файл с расширением .pickle
    pickle.dump(workers, open("workers.p", "wb")) 



def del_id(id): # Метод удаления записи из телефонного справочника
    del workers[id]
    pickle.dump(workers, open("workers.p","wb" ))


def export_txt_format(file): # Экспортируем данные из телефонной книги в файл формата .txt
        with open(file, 'w') as file:
            for line in workers.items():
                file.write(str(line) + '\n')


def export_csv_format(file): # Экспортируем данные из телефонной книги в файл формата .csv

    with open(file, 'w') as file_1:
        file_1.write('id; FIO; birth_date; work_place; tel_number_personal; tel_number_working\n')
        for i,r in workers.items():
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

def export_json_format(file): # Экспортируем данные о сотрудниках в файл формата .json
    with open(file, "w") as write_file:
        for i in workers.items():
            write_file.write('id_' + str(i) + '\n')
            
print(workers)
export_json_format('workers.json')







