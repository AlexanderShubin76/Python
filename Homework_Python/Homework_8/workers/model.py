# Модуль отвечает за внутреннюю логику программы. 
# Здесь хранятся 3 группы методов.
# 1-я группа методов необходима для проведения выборки по сотрудникам.
# 2-я группа методов представлена методами для добавления, удаления, обновления данных о сотруднике.
# 3-я группа методов необходима для экспорта данных о сотрудниках в форматы .csv или .json.
# Данные о сотрудниках хранятся в файле "workers.p". Данные о сотрудниках включает следующие поля:
# id, last_name, first_name, post, tel_number, salary.

import pickle
import json

# workers = {
#      '1': {'last_name': 'Иванов', 'first_name': 'Иван', 'post': 'Инженер-химик', \
#          'tel_number': '878', 'salary': 95000},
#      '2': {'last_name': 'Петров', 'first_name': 'Сергей', 'post': 'Электрик', \
#          'tel_number': '578', 'salary': 60000},
#      '3': {'last_name': 'Васильев', 'first_name': 'Александр', 'post': 'Водитель', \
#         'tel_number': '222', 'salary': 62000},
#      '4': {'last_name': 'Сидорова', 'first_name': 'Алена', 'post': 'Бухгалтер', \
#          'tel_number': '423', 'salary': 75000},
#      '5': {'last_name': 'Куликова', 'first_name': 'Светлана', 'post': 'Менеджер по продажам', \
#          'tel_number': '312', 'salary': 80000}
#  }

# pickle.dump(workers, open("workers.p","wb" ))
#  Извлекаем наш измененный при предыдущих запусках программы словарь из файла с расширением .pickle
workers = pickle.load(open( "workers.p", "rb" ) ) 

def search_worker(id): # метод поиска сотрудника по id
    if id in workers.keys():
        print(f'По id_{id} найден следующий сотрудник: {workers[id]}')
    else:
        print('Сотрудников с таким id не обнаружено')

def search_post(position): # метод поиск сотрудника по должности'
    str = ''
    for k,v in workers.items():
        if position == v['post']:
            str += f'id_{k}: {v}' + '\n'
            print(f'C должностью "{position}" найдены следующие сотрудники: ')
            print(str)
    if str == '':
        print(f'С должностью "{position}" сотрудников не обнаружено!')

def search_salary(min_value, max_value): # метод выборки сотрудников по зарплате
    str = ''
    for k,v in workers.items():
        if min_value<=v['salary']<= max_value:
            str += f'id_{k}: {v}' + '\n'
            print(f'C уровнем зарплаты от {min_value} до {max_value} найдены следующие сотрудники: ')
            print(str)
    if str == '':
        print(f'C уровнем зарплаты от {min_value} до {max_value} сотрудников не найдено!')

def add_id(id, last_name, first_name, post, tel_number, salary): # Метод добавления записи в cловарь.
    workers[id] = {'last_name': last_name, 'first_name': first_name, \
        'post': post, 'tel_number': tel_number, 'salary': salary}
    print('Запись добавлена!')
    #Чтобы изменения сохранились, добавляем словарь с изменениями в файл с расширением .pickle
    pickle.dump(workers, open("workers.p", "wb")) 

def del_id(id): # Метод удаления записи из словаря
    del workers[id]
    print('Данные о сотруднике удалены')
    #Чтобы изменения сохранились, добавляем словарь с изменениями в файл с расширением .pickle
    pickle.dump(workers, open("workers.p","wb" ))

def rewrite_id(id, last_name, post, tel_number, salary): # Метод изменения записи в cловаре.
    workers[id] = {'last_name': last_name, 'first_name': workers[id]['first_name'], \
        'post': post, 'tel_number': tel_number, 'salary': salary}
    print(' Данные сотрудника изменены!')
    #Чтобы изменения сохранились, добавляем словарь с изменениями в файл с расширением .pickle
    pickle.dump(workers, open("workers.p", "wb")) 

def export_csv_format(file): # Экспортируем данные из словаря в файл формата .csv
    with open(file, 'w') as file_1:
        file_1.write('id; last_name; first_name; post; tel_number; salary\n')
        for i,r in workers.items():
            id = i
            last_name = r['last_name']
            first_name = r['first_name']
            post = r['post']
            tel_number = r['tel_number']
            salary = r['salary']
            file_1.write(f'{id}; {last_name}; {first_name}; {post}; {tel_number}; {salary}\n')
        print('Экспорт данных успешно произведен!')

def export_json_format(file): # Экспортируем данные о сотрудниках в файл формата .json
    with open(file, 'w') as f:
        for d in workers.items():
            json.dump(workers, f)
            f.write('\n')
        print('Экспорт данных успешно произведен!')
