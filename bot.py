import telebot
from datetime import datetime
import time
bot = telebot.TeleBot('1009814377:AAHUvKXpCfiuxlwZ0lJ9U7T3ZhjPdjLUIrs')
now = datetime.now()
#functions
@bot.message_handler(commands = ['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Hi!' )
@bot.message_handler(commands = ['time'])
def time_now(message):
    bot.send_message(message.chat.id, time.strftime('%I:%M %p') )
@bot.message_handler(commands = ['date'])
def date_today(message):
    bot.send_message(message.chat.id, now.strftime("%d-%m-%Y"))
@bot.message_handler(commands = ['dayofweek'])
def day_of_week(message):
    bot.send_message(message.chat.id, now.strftime('%A'))
@bot.message_handler(commands = ['cat'])
def hint(message):
    bot.send_photo(message.chat.id, 'AgACAgIAAxkBAAP1Xkhc5pfWjBvVIHjXSnHME9NuwVgAAoCuMRu2U0BKHT45zetIOKd9Y8sOAAQBAAMCAAN5AAMRTgIAARgE')
@bot.message_handler(content_types = ['photo'])
def photo_id(message):
    print(message)
bot.polling()
