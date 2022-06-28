import telebot 
from telebot import types
import random
import datetime
import numpy as np
token = "5525229543:AAF5zhi0s34PWgg0x3ufwdEAnxrrgCCLpjY"  # токен для подключения к Боту

bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(content_types=['text'])  
def chatting(message):
    if message.text == '/start' or message.text.lower() == 'вернуться в главное меню':  # кнопки главного меню
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Расписания')
        btn2 = types.KeyboardButton('Основные подразделения')
        btn3 = types.KeyboardButton('Корпуса')
        btn4 = types.KeyboardButton('Полезные ссылки')
        btn5 = types.KeyboardButton('Мероприятия')
        btn6 = types.KeyboardButton('Консультации')
        btn7 = types.KeyboardButton('Заметки')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.chat.id, 'Здравствуйте, я - информационный бот VSTU для помощи студентам.', reply_markup=markup)

    if  message.text.lower() == 'корпуса':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # кнопки корпусов
        btn1 = types.KeyboardButton('Высотный учебный корпус')
        btn2 = types.KeyboardButton('Главный учебный корпус')
        btn3 = types.KeyboardButton('А учебный корпус')
        btn4 = types.KeyboardButton('Б учебный корпус')
        btn5 = types.KeyboardButton('Кировский учебный корпус')
        btn6 = types.KeyboardButton('Красноармейский учебный корпус')
        btn_exit = types.KeyboardButton('Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn_exit)
        bot.send_message(message.chat.id, 'Предоставляю информацию о корпусах ВолгГТУ в Волгограде:', reply_markup=markup)




        #bot.send_photo(message.from_user.id, 'https://yandex.ru/images/search?from=tabbar&text=корпус%20высотки%20волггту&pos=0&img_url=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F7%2F74%2FVysotnyy_korpus.jpg%2F400px-Vysotnyy_korpus.jpg&rpt=simage&lr=10954')

    


    # if message.text == 'корпус':
    #     img = open('Vkorpus.jpg', 'rb')
    #     bot.send_photo(message.from_user.id, img)


# @bot.message_handler(func=lambda message: True) # функция "попугай"
# def echo_all(message):
# 	bot.reply_to(message, message.text)

bot.infinity_polling()