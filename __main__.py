import telebot
import numpy as np

bot = telebot.TeleBot("5525229543:AAF5zhi0s34PWgg0x3ufwdEAnxrrgCCLpjY", parse_mode=None)

@bot.message_handler(func=lambda message: True) # функция "попугай"
def echo_all(message):
	bot.reply_to(message, message.text)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Я тебе НЕ бот!")

@bot.message_handler(content_types=['text'])   # функция для удаления сообщения  сзапретным словом
def chatting(message):
    if message.text.lower() =='слово':
        bot.delete_message(message.chat.id, message.message_id)

bot.infinity_polling()