import telebot
import random
import datetime
import numpy as np

TOKEN = "5525229543:AAF5zhi0s34PWgg0x3ufwdEAnxrrgCCLpjY"  # токен для подключения к Боту

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(content_types=['text'])   # функция для удаления сообщения  сзапретным словом
def chatting(message):

    if message.text == '/start' or  message.text == '/help': 
        bot.reply_to(message, 'Я тебе НЕ бот!')

    if message.text.lower() =='слово':
        bot.delete_message(message.chat.id, message.message_id)

    if  message.text == '/random':
        bot.send_message(message.from_user.id, random.randint(0,9))
    
    if  message.text == '/time':
        bot.send_message(message.from_user.id, str(datetime.datetime.now()))





# @bot.message_handler(func=lambda message: True) # функция "попугай"
# def echo_all(message):
# 	bot.reply_to(message, message.text)

bot.infinity_polling()