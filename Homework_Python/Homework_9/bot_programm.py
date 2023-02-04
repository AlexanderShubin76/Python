# Создал бота в тг для выполнения простейших арифметических операция
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

def hello(update: Update, context: ContextTypes.DEFAULT_TYPE): # Метод для приветствия пользователя
    return update.message.reply_text(f'Привет {update.effective_user.first_name}!!!')

def calc(update: Update, context: ContextTypes.DEFAULT_TYPE): # Метод, выполняющий арифметические операции.
  
    msg = update.message.text #записываем сообщение в переменную
    print(msg)
    items = msg.split() # /sum  123 43423
    x = float(items[1])
    y = float(items[3])
    if items[2] == '-':
        return update.message.reply_text(f'{x} - {y} = {x-y}')
    if items[2] == '+':
        return update.message.reply_text(f'{x} + {y} = {x+y}')
    if items[2] == '/':
        return update.message.reply_text(f'{x} / {y} = {round(x/y, 5)}')
    if items[2] == '*':
        return update.message.reply_text(f'{x} * {y} = {round(x * y, 5)}')
    else:
        return update.message.reply_text('Ошибка ввода. Доступны только операции: "+", "-", "/", "*"!')

app = ApplicationBuilder().token("6131920884:AAEXXhkBKxpAMcudFHEJcgxvkBjNBjvcziM").build()

app.add_handler(CommandHandler("calc", calc))
app.add_handler(CommandHandler("hello", hello))

print('server start')
app.run_polling()