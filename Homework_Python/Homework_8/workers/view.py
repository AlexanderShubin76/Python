# В данном модуле написаны методы, посредством которых пользователь взаимодействует с модулем model.
# Пользователь выбирать какие изменения он хочет внести в базу данными с сотрудниками.

import model as md

def show_menu() -> int: # Метод для выбора пользователем действий над базой данных.
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    num = int(input("Введите номер необходимого действия: "))
    while (not 1<=num<=9):
            num = int(input("Ошибка ввода. Введите номер необходимого действия: "))
    return num
    
def get_id(): # Метод для ввода id сотрудника
    return input('Введите номер id сотрудника: ')
    
    
def print_workers(): # Метод для печать базы данных сотрудников
    for i in md.workers.items():
            print(f'{i}\n')

def get_position(): # Метод для ввода должности
    return input('Введите название должности, которую хотите найти с заглавной буквы: ')

def get_salary(): # Метод для ввода диапазона заработной платы:
    min_value = int(input('Введите нижнюю границу заработной платы для поиска: '))
    max_value = int(input('Введите верхнюю границу заработной платы для поиска: '))
    while(max_value<= min_value):
        max_value = int(input('Ошибка ввода. Введите верхнюю границу заработной платы для поиска.\
        Она должна быть выше нижней границы: '))
    return min_value, max_value


# # С помощью данного метода задаем новые данные для внесения в словарь, представляющий собой базу данных сотрудников.
def new_id(): 
    id = get_id()
    while (id in md.workers.keys()):
        id = input('Такой id существует. Введите уникальное значение id в цифровом виде для новой записи: ')
    last_name = input('Введите фамилию сотрудника: ') # id, last_name, first_name, post, tel_number, salary.
    first_name = input('Введите имя сотрудника: ')
    post = input('Введите должность сотрудника: ')
    tel_number = input('Введите телефонный номер сотрудника: ')
    salary = int(input('Введите размер зарплаты сотрудника в целочисленном виде: '))
    return (id, last_name, first_name, post, tel_number, salary)

def remove_id(): # С помощью данного метода указывем id сотрудника, которого хотим удалить.
    rem_id = get_id()
    while (rem_id not in md.workers.keys()):
        rem_id = input('Такой id не существует. Введите значение id сотрудника, которого хотите удалить: ')
    return rem_id

def rerecord_id(): # С помощью данного метода изменяем данные сотрудника.
    id = get_id()
    while (id not in md.workers.keys()):
        id = input('Такой id не существует. Введите значение id сотрудника, данные которого хотите обновить: ')
    last_name = input('Введите новую фамилию сотрудника. Если фамилию не нужно менять, нажмите " ": ')
    if last_name  == " ":
        last_name = md.workers[id]['last_name']
    post = input('Введите должность сотрудника. Если должность не нужно менять, нажмите " ": ')
    if post  == " ":
        post = md.workers[id]['post']
    tel_number = input('Введите телефонный номер сотрудника. Если телефон не нужно менять, нажмите " ": ')
    if  tel_number == " ":
        tel_number = md.workers[id]['tel_number']
    salary = int(input('Введите размер зарплаты сотрудника в целочисленном виде. Если зарплату не нужно менять, нажмите "0": '))
    if  salary == "0":
        salary = md.workers[id]['salary']
    return (id, last_name, post, tel_number, salary)

