# ����� ����� ������� ������ send_btn,�� ���������� �����-�� ��������� ���� �������
def send_message(message):
    user = message.chat.id
    with open("hackaton.json", "r+") as file:
        admins = json.load(file)   
        for target in admins["admins"]:
            bot.send_message(int(target), "� ������� ��� ��� ���������,������ ��� �� �����.")
def help(message):
    user = message.chat.id
    keyboard = types.InlineKeyboardMarkup()
    with open("hackaton.json", "r+") as file:
        admins = json.load(file)
        admin_id=str(message.chat.id)  
        if admin_id in admins["admins"]:  
            send_btn=types.InlineKeyboardButton(text="��������� ���� ������� ����� ����������", callback_data="send_btn")
            keyboard.add(send_btn)
    # ��������� �� ��� 2 ������
    start_btn = types.InlineKeyboardButton(text="����������", callback_data="start_btn")
    try_admin_btn = types.InlineKeyboardButton(text="� �����", callback_data="try_admin_btn")
    keyboard.add(start_btn)
    keyboard.add(try_admin_btn) 
    bot.send_message(user, "��� ����������,�������� ��������", reply_markup=keyboard)
def check_admin(message):
    user = message.chat.id
    if message.text=="myinvite":
        with open("hackaton.json", "r+") as file:
            admins = json.load(file)
            admin_id=str(message.from_user.id)  
            if admin_id in admins["admins"]:
                bot.send_message(user, "�� ��� ��������� �������,��� �� ��������� ������� ������", reply_markup=keyboard)   
            else :
                bot.send_message(message.chat.id, "�� ����� ������. ������ �� �����.")
                admins["admins"].append(admin_id)
                json.dump(admins, file)
        with open("hackaton.json", "r+") as file:
                json.dump(admins, file)
    else:
        bot.send_message(message.chat.id, "�� ����� �������� ������."+"\n"+ "�� �� ���� ��������� � ������ �������")
import telebot
import json
from random import shuffle
from telebot import types 
token = "902830179:AAH8DXEfgCIzE4U_PKme84_6Prg9bXjaJuQ"

# ������� ���������� � ������� ������
telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}

# ������������ � ���������
bot = telebot.TeleBot(token=token)
# � ������ �������� ������� myinvite �������� ��������� �������� 
@bot.message_handler(commands=['start'])
def help(message):
    user = message.chat.id
    keyboard = types.InlineKeyboardMarkup()
    with open("hackaton.json", "r") as file:
        admins = json.load(file)
        admin_id=str(message.chat.id)  
        if admin_id in admins["admins"]:  
            send_btn=types.InlineKeyboardButton(text="��������� ���� ������� ����� ����������", callback_data="send_btn")
            keyboard.add(send_btn)
    # ��������� �� ��� 2 ������
    start_btn = types.InlineKeyboardButton(text="����������", callback_data="start_btn")
    try_admin_btn = types.InlineKeyboardButton(text="� �����", callback_data="try_admin_btn")
    keyboard.add(start_btn)
    keyboard.add(try_admin_btn) 
    bot.send_message(user, "��� ����������,�������� ��������", reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)        
def callback_inline(call):
    if call.message:
        if call.data == "start_btn":
            msg=bot.send_message(call.message.chat.id, "������ �� �������� ����������!!")
            help(msg)
        if call.data == "try_admin_btn":
            bot.send_message(call.message.chat.id, "������� ������.")
        if call.data == "send_btn":
            msg=bot.send_message(call.message.chat.id, "��� ��������� ���� ��������� �������")
            send_message(msg)
@bot.message_handler(content_types=['text'])
def check_admin(message):
    user = message.chat.id
    if message.text=="myinvite":
        with open("hackaton.json", "r+") as file:
            admins = json.load(file)
            admin_id=str(message.from_user.id)  
            if admin_id in admins["admins"]:
                bot.send_message(user, "�� ��� ��������� �������,��� �� ��������� ������� ������")   
            else :
                bot.send_message(message.chat.id, "�� ����� ������. ������ �� �����.")
                admins["admins"].append(admin_id)
        with open("hackaton.json", "r+") as file:
            json.dump(admins, file)   
    else:
        mas = ["��","��","�����","���������","��","����","����������"]
        shuffle(mas)
        bot.send_message(message.chat.id," ".join(mas))
# ������� - ������ ���� � ����������� �������� ���������
bot.polling(none_stop=True)
