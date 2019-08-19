# когда админ кликает кнопку send_btn,он отправляет какое-то сообщение всем админам
def send_message(message):
    user = message.chat.id
    with open("hackaton.json", "r+") as file:
        admins = json.load(file)   
        for target in admins["admins"]:
            bot.send_message(int(target), "Я прислал вам это сообщение,Потому что вы админ.")
def help(message):
    user = message.chat.id
    keyboard = types.InlineKeyboardMarkup()
    with open("hackaton.json", "r+") as file:
        admins = json.load(file)
        admin_id=str(message.chat.id)  
        if admin_id in admins["admins"]:  
            send_btn=types.InlineKeyboardButton(text="Разослать всем админам число участников", callback_data="send_btn")
            keyboard.add(send_btn)
    # добавляем на нее 2 кнопки
    start_btn = types.InlineKeyboardButton(text="Инструкция", callback_data="start_btn")
    try_admin_btn = types.InlineKeyboardButton(text="Я админ", callback_data="try_admin_btn")
    keyboard.add(start_btn)
    keyboard.add(try_admin_btn) 
    bot.send_message(user, "Это инструкция,выберите кнопочку", reply_markup=keyboard)
def check_admin(message):
    user = message.chat.id
    if message.text=="myinvite":
        with open("hackaton.json", "r+") as file:
            admins = json.load(file)
            admin_id=str(message.from_user.id)  
            if admin_id in admins["admins"]:
                bot.send_message(user, "Вы уже являетесь админом,вам не требуется вводить инвайт", reply_markup=keyboard)   
            else :
                bot.send_message(message.chat.id, "Вы ввели инвайт. Теперь вы админ.")
                admins["admins"].append(admin_id)
                json.dump(admins, file)
        with open("hackaton.json", "r+") as file:
                json.dump(admins, file)
    else:
        bot.send_message(message.chat.id, "Вы ввели неверный инвайт."+"\n"+ "Вы не были добавлены в список админов")
import telebot
import json
from random import shuffle
from telebot import types 
token = "902830179:AAH8DXEfgCIzE4U_PKme84_6Prg9bXjaJuQ"

# Обходим блокировку с помощью прокси
telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}

# подключаемся к телеграму
bot = telebot.TeleBot(token=token)
# в данной ситуации команда myinvite является админским инвайтом 
@bot.message_handler(commands=['start'])
def help(message):
    user = message.chat.id
    keyboard = types.InlineKeyboardMarkup()
    with open("hackaton.json", "r") as file:
        admins = json.load(file)
        admin_id=str(message.chat.id)  
        if admin_id in admins["admins"]:  
            send_btn=types.InlineKeyboardButton(text="Разослать всем админам число участников", callback_data="send_btn")
            keyboard.add(send_btn)
    # добавляем на нее 2 кнопки
    start_btn = types.InlineKeyboardButton(text="Инструкция", callback_data="start_btn")
    try_admin_btn = types.InlineKeyboardButton(text="Я админ", callback_data="try_admin_btn")
    keyboard.add(start_btn)
    keyboard.add(try_admin_btn) 
    bot.send_message(user, "Это инструкция,выберите кнопочку", reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)        
def callback_inline(call):
    if call.message:
        if call.data == "start_btn":
            msg=bot.send_message(call.message.chat.id, "Сейчас вы получите инструкцию!!")
            help(msg)
        if call.data == "try_admin_btn":
            bot.send_message(call.message.chat.id, "Введите инвайт.")
        if call.data == "send_btn":
            msg=bot.send_message(call.message.chat.id, "Это сообщение было разослано админам")
            send_message(msg)
@bot.message_handler(content_types=['text'])
def check_admin(message):
    user = message.chat.id
    if message.text=="myinvite":
        with open("hackaton.json", "r+") as file:
            admins = json.load(file)
            admin_id=str(message.from_user.id)  
            if admin_id in admins["admins"]:
                bot.send_message(user, "Вы уже являетесь админом,вам не требуется вводить инвайт")   
            else :
                bot.send_message(message.chat.id, "Вы ввели инвайт. Теперь вы админ.")
                admins["admins"].append(admin_id)
        with open("hackaton.json", "r+") as file:
            json.dump(admins, file)   
    else:
        mas = ["Вы","не","админ","отстаньте","от","меня","пожалуйста"]
        shuffle(mas)
        bot.send_message(message.chat.id," ".join(mas))
# поллинг - вечный цикл с обновлением входящих сообщений
bot.polling(none_stop=True)
