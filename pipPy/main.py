# 1. Определение четное ли число
# from isOdd import isOdd

# # print(isOdd('1')) #//=> true
# # print(isOdd('5')) #//=> true

# print(isOdd(0)) #//=> false
# print(isOdd(4)) #//=> false

# 2. Отслеживание прогресса выполнения программы
# from progress.bar import Bar
# import time
# bar = Bar('Processing', max=20)
# for i in range(20):
#     # Do some work
#     time.sleep(1)
#     bar.next()
# bar.finish()

# 3. emoji
# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))

# # 4. Построить график

# import matplotlib.pyplot as plt
# import numpy as np

# list = [1,2,3,2,7]
# plt.plot(list)
# plt.show()

# 5. telegram bot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import hi_command
from bot_commands import time_command
from bot_commands import help_command
from bot_commands import sum_command


app = ApplicationBuilder().token("6080940692:AAG_F6sCPQcG-TmzYutH8QqbVBNbu3myyWA").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))


print('server start')
app.run_polling()