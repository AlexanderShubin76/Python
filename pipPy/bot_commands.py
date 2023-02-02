from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *
def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    return update.message.reply_text(f'Hi {update.effective_user.first_name}!!!')

def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    return update.message.reply_text(f'/hi\n/time\n/help')

def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    return update.message.reply_text(f'{datetime.datetime.now().time()}')

def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text #записываем сообщение в переменную
    print(msg)
    items = msg.split() # /sum  123 43423
    x = int(items[1])
    y = int(items[2])

    return update.message.reply_text(f'{x} + {y} = {x+y}')    