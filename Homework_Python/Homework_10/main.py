import telebot
from telebot import types
bot = telebot.TeleBot('6131920884:AAEXXhkBKxpAMcudFHEJcgxvkBjNBjvcziM')

@bot.message_handler(commands = ['start']) # прописываем отслеживание команд

def start(message):
     mess = f'Привет,{message.from_user.first_name}'
     bot.send_message(message.chat.id,mess)  # вывод данных пользователю(1-й параметр куда будем отправлять сообщение(чат)

# @bot.message_handler(content_types=['text']) #отслеживаем текст от пользователя
# def get_user_text(message):
#      if message.text == "Hello":
#           bot.send_message(message.chat.id, 'Здорова, пацан')
#      elif message.text == 'id':
#           bot.send_message(message.chat.id, f'Твой id: {message.from_user.id}')
#      elif message.text == 'photo':
#           photo = open('67130346.png', 'rb')
#           bot.send_photo(message.chat.id, photo)
#      else:
#           bot.send_message(message.chat.id, 'Не понимаю')

@bot.message_handler(content_types=['photo']) #отслеживание контента(фото, видео)

def get_user_photo(message):
     bot.send_message(message.chat.id, 'Ты крут, чувак')

@bot.message_handler(commands = ['website'])
def website(message):
     markup = types.InlineKeyboardMarkup()    #types - объект через которого создаем кнопки. Данный класс позволяет создавать встроенные в сообщения кнопки,изображения
     markup.add(types.InlineKeyboardButton('Посетить веб-сайт', url = 'https://dzen.ru'))  #скомпоновать в единую структуру
     bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup = markup) # прикрепить фото

@bot.message_handler(commands = ['help'])
def website(message):
     markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)    #types - объект через которого создаем кнопки. Создает кнопки в поле ввода
     website = types.KeyboardButton('Веб сайт')  # Создаем кнопку
     start = types.KeyboardButton('Старт')


     markup.add(website, start)  #скомпоновать в единую структуру
     bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup = markup) # прикрепить фото

bot.polling(none_stop=True) #запустить бота на постоянную обработку