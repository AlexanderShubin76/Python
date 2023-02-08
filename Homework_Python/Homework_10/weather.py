# Здесь написан код для бота, показывающего погоду при вводе названия города
import datetime
import requests
import telebot
from telebot import types

bot = bot = telebot.TeleBot('6131920884:AAEXXhkBKxpAMcudFHEJcgxvkBjNBjvcziM') #привязываем токен нашего бота
weather_token = '9c5e25b2003dfb2243ed13c338906758' # записываем токен с сайта https://openweathermap.org/

def show_weather(weather_city, weather_token): #
    try:
        result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={weather_city}'
                              f'&appid={weather_token}&units=metric') # формируем наш запрос
        data = result.json()
        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']


        return f'Текущее время: {datetime.datetime.now().strftime("%d-%m-%Y %H:%M")}\n'\
        f'Температура: {temperature} °C \n'\
        f'Влажность: {humidity} % \n'\
        f'Давление: {pressure} мм.рт.ст \n'\
        f'Скорость ветра: {wind_speed} м/с \n'

    except Exception:
        return 'Ошибка. Данный город не могу найти ((('

@bot.message_handler(commands = ['start']) # прописываем отслеживание команд

def start(message):
     mess = f'Привет, {message.from_user.first_name}\n' \
            f'Введи название города, где хочешь узнать погоду!!!'

     bot.send_message(message.chat.id, mess) # вывод данных пользователю

@bot.message_handler(content_types=['text']) #отслеживаем текст от пользователя
def get_weather(message):
    mess = show_weather(message.text, weather_token)
    bot.send_message(message.chat.id, mess)


bot.polling(none_stop=True)