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

    if  message.text == 'Корпуса':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # кнопки корпусов
        btn1 = types.KeyboardButton('Высотный учебный корпус')
        btn2 = types.KeyboardButton('Главный учебный корпус')
        btn3 = types.KeyboardButton('А учебный корпус')
        btn4 = types.KeyboardButton('Б учебный корпус')
        btn5 = types.KeyboardButton('Тракторный учебный корпус')
        btn6 = types.KeyboardButton('Кировский учебный корпус')
        btn7 = types.KeyboardButton('Красноармейский учебный корпус')
        btn_exit = types.KeyboardButton('Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn_exit)
        bot.send_message(message.chat.id, 'Предоставляю информацию о корпусах ВолгГТУ в Волгограде:', reply_markup=markup)

    if message.text == 'Высотный учебный корпус':
        bot.send_photo(message.from_user.id, 'https://yandex.ru/images/search?from=tabbar&text=корпус%20высотки%20волггту&pos=0&img_url=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F7%2F74%2FVysotnyy_korpus.jpg%2F400px-Vysotnyy_korpus.jpg&rpt=simage&lr=10954')
        bot.send_message(message.chat.id, 'Высотный учебный корпус. Адрес: Волгоград, проспект им. Ленина, 28а')
    if message.text == 'Главный учебный корпус':
        bot.send_photo(message.from_user.id, 'https://yandex.ru/images/search?from=tabbar&text=гук%20волггту&pos=0&img_url=https%3A%2F%2Fi5.photo.2gis.com%2Fimages%2Fbranch%2F33%2F4644337147616648_ef42.jpg&rpt=simage&lr=10954')
        bot.send_message(message.chat.id, 'Главный учебный корпус. Адрес: Волгоград, проспект им. Ленина, 28')
    if message.text == 'А учебный корпус':
        bot.send_photo(message.from_user.id, 'https://yandex.ru/images/search?from=tabbar&text=а%20корпус%20волггту&pos=11&img_url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-altay%2F374295%2F2a0000015b3b5b6036aeea146e364f4803ec%2FXXL&rpt=simage&lr=10954')
        bot.send_message(message.chat.id, 'А учебный корпус. Адрес: Волгоград, Советская, 31')
    if message.text == 'Б учебный корпус':
        bot.send_photo(message.from_user.id, 'https://yandex.ru/images/search?text=Учебный%20корпус%204%20ВГТУ&source=related-duck&lr=10954&from=tabbar&pos=4&rpt=simage&img_url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-altay%2F758957%2F2a00000161ca5e6cc553f88c77e9c09fc85c%2FXXL')
        bot.send_message(message.chat.id, 'Б учебный корпус. Адрес: Волгоград, Советская, 29')
    if message.text == 'Тракторный учебный корпус':
        bot.send_photo(message.from_user.id, 'https://yandex.ru/images/search?from=tabbar&text=тракторный%20корпус%20волггту&pos=3&img_url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-altay%2F492546%2F2a0000015eb1ae89cbbcdd9463804000e983%2FXXL&rpt=simage&lr=10954')
        bot.send_message(message.chat.id, 'Тракторный учебный корпус. Адрес: Волгоград, Дегтярёва, 2')
    if message.text == 'Кировский учебный корпус':
        bot.send_photo(message.from_user.id, 'https://yandex.ru/images/search?text=Кировский%20Вечерний%20Факультет%20ВОЛГГТУ&source=related-duck&lr=10954&from=tabbar&pos=0&rpt=simage&img_url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-altay%2F1773749%2F2a0000016da63addc1782894061d220fddc0%2FXXL&rlt_url=%2F%2Favatars.mds.yandex.net%2Fi%3Fid%3D9fa885f43ce094334ff077ca6f459d5f_l-5235887-images-thumbs%26ref%3Drim%26n%3D13%26w%3D1080%26h%3D1080&ogl_url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-altay%2F1773749%2F2a0000016da63addc1782894061d220fddc0%2FXXL')
        bot.send_message(message.chat.id, 'Кировский учебный корпус. Адрес: Волгоград, Армавирская, 15')        
    if message.text == 'Красноармейский учебный корпус':
        bot.send_photo(message.from_user.id, 'https://yandex.ru/images/search?from=tabbar&text=красноармейский%20корпус%20волггту%20фото&pos=0&img_url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-altay%2F1627037%2F2a00000167ecc7f0f217c356d9fd33adddf3%2FXXL&rpt=simage&lr=10954')
        bot.send_message(message.chat.id, 'Красноармейский учебный корпус. Адрес: Волгоград, проспект Столетова, 8')        

       


    # if message.text == 'корпус':
    #     img = open('Vkorpus.jpg', 'rb')
    #     bot.send_photo(message.from_user.id, img)


# @bot.message_handler(func=lambda message: True) # функция "попугай"
# def echo_all(message):
# 	bot.reply_to(message, message.text)

bot.infinity_polling()