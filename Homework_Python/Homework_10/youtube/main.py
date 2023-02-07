import telebot

bot = telebot.Telebot('6131920884:AAEXXhkBKxpAMcudFHEJcgxvkBjNBjvcziM')

@bot.messahe_handlers(commands = ['start']) # прописываем отслеживание команд

def start(message):
    mess = f'Привет,{message.from_user.first_name}'
    bot.send_message(message.chat.id, mess) #вывод данных пользователю(1-й параметр куда будем отправлять сообщение(чат)

@

bot.polling(none stop=True) #запустить бота на постоянную обработку