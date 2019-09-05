import telebot
import database

menu=telebot.types.ReplyKeyboardMarkup(True, False)
menu.row('Расписание')
menu.row('Изменения')
menu.row('Домашка')

bot=telebot.TeleBot("945462714:AAH0ikBMSiiiwjDBOafR_ZA_5D_o_jW_cPo")

@bot.message_handler(content_types=['text'])
def start(message):

    if message.text=='/start':
        bot.send_message(message.from_user.id,'Привет, что тебе нужно?',reply_markup=menu)

    if message.text=='Расписание':    
        keyboard=telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard.row('Понедельник','Вторник')
        keyboard.row('Среда','Четверг')
        keyboard.row('Пятница','Субота')
        keyboard.row('Назад')
        bot.send_message(message.from_user.id,'На какой день недели?',reply_markup=keyboard)

    if message.text=='Назад':
        bot.send_message(message.from_user.id,'Привет, что тебе нужно?',reply_markup=menu)


    if message.text=='Понедельник' and database.chet == 'Чет':
        bot.send_message(message.chat.id,database.mon2)

    if message.text=='Понедельник' and database.chet == 'Нечет':
        bot.send_message(message.chat.id,database.mon1)

    if message.text=='mon1change':
        sent_1 = bot.send_message(message.chat.id,'Введи Расписание')
        bot.register_next_step_handler(sent_1,mon1)

    if message.text=='mon2change':
        sent_1 = bot.send_message(message.chat.id,'Введи Расписание')
        bot.register_next_step_handler(sent_1,mon2)


    if message.text=='Вторник' and database.chet == 'Чет':
        bot.send_message(message.chat.id,database.tues2)

    if message.text=='Вторник' and database.chet == 'Нечет':
        bot.send_message(message.chat.id,database.tues1)

    if message.text=='tues1change':
        sent_1 = bot.send_message(message.chat.id,'Введи Расписание')
        bot.register_next_step_handler(sent_1,tues1)

    if message.text=='tues2change':
        sent_1 = bot.send_message(message.chat.id,'Введи Расписание')
        bot.register_next_step_handler(sent_1,tues2)


    if message.text=='Среда' and database.chet == 'Чет':
        bot.send_message(message.chat.id,database.wed2)

    if message.text=='Среда' and database.chet == 'Нечет':
        bot.send_message(message.chat.id,database.wed1)

    if message.text=='wed1change':
        sent_1 = bot.send_message(message.chat.id,'Введи Расписание')
        bot.register_next_step_handler(sent_1,wed1)

    if message.text=='wed2change':
        sent_1 = bot.send_message(message.chat.id,'Введи Расписание')
        bot.register_next_step_handler(sent_1,wed2)


    if message.text=='Четверг' and database.chet == 'Чет':
        bot.send_message(message.chat.id,database.thurs2)

    if message.text=='Четверг' and database.chet == 'Нечет':
        bot.send_message(message.chat.id,database.thurs1)

    if message.text=='tues1change':
        sent_1 = bot.send_message(message.chat.id,'Введи Расписание')
        bot.register_next_step_handler(sent_1,thurs1)

    if message.text=='tues2change':
        sent_1 = bot.send_message(message.chat.id,'Введи Расписание')
        bot.register_next_step_handler(sent_1,thurs2)


    if message.text=='Пятница' and database.chet == 'Чет':
        bot.send_message(message.chat.id,database.fri2)

    if message.text=='Пятница' and database.chet == 'Нечет':
        bot.send_message(message.chat.id,database.fri1)

    if message.text=='fri1change':
        sent_1 = bot.send_message(message.chat.id,'Введи Расписание')
        bot.register_next_step_handler(sent_1,fri1)

    if message.text=='fri2change':
        sent_1 = bot.send_message(message.chat.id,'Введи Расписание')
        bot.register_next_step_handler(sent_1,fri2)


    if message.text== 'Субота' and database.chet == 'Чет':
        bot.send_message(message.chat.id,database.sat2)

    if message.text== 'Субота' and database.chet == 'Нечет':
        bot.send_message(message.chat.id,database.sat1)

    if message.text=='sat1change':
        sent_1 = bot.send_message(message.chat.id,'Введи Расписание')
        bot.register_next_step_handler(sent_1,sat1)

    if message.text=='sat2change':
        sent_1 = bot.send_message(message.chat.id,'Введи Расписание')
        bot.register_next_step_handler(sent_1,sat2)


    if message.text=='Четн':
        sent_1 = bot.send_message(message.chat.id,'Введи Чётность')
        bot.register_next_step_handler(sent_1, chet1)


    if message.text=='Домашка':
        keyboard=telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard.row('Основы алгоритмов и программирования')
        keyboard.row('Устройство и функционирование ИС')
        keyboard.row('Элементы высшей математики')
        keyboard.row('Русский язык и культура речи')
        keyboard.row('Инглишь')
        keyboard.row('Физра')
        keyboard.row('МДК')
        keyboard.row('БЖ')
        keyboard.row('Назад')
        bot.send_message(message.chat.id,'На какой предмет?',reply_markup=keyboard)

    if message.text=='Основы алгоритмов и программирования':
        bot.send_message(message.chat.id,database.les1)

    if message.text=='Устройство и функционирование ИС':
        bot.send_message(message.chat.id,database.les2) 

    if message.text=='Элементы высшей математики':
        bot.send_message(message.chat.id,database.les3)

    if message.text=='Русский язык и культура речи':
        bot.send_message(message.chat.id,database.les4)

    if message.text=='Инглишь':
        bot.send_message(message.chat.id,database.les5)

    if message.text=='Физра':
        bot.send_message(message.chat.id,database.les6)

    if message.text=='МДК':
        bot.send_message(message.chat.id,database.les7)

    if message.text=='БЖ':
        bot.send_message(message.chat.id,database.les8)                


    if message.text=='Админ на месте':
        keyboard=telebot.types.ReplyKeyboardMarkup(True, False)
        keyboard.row('#Основы алгоритмов и программирования#')
        keyboard.row('#Устройство и функционирование ИС#')
        keyboard.row('#Элементы высшей математики#')
        keyboard.row('#Русский язык и культура речи#')
        keyboard.row('#Инглишь#')
        keyboard.row('#Физра#')
        keyboard.row('#МДК#')
        keyboard.row('#БЖ#')
        keyboard.row('Назад')
        bot.send_message(message.chat.id,'На какой предмет?',reply_markup=keyboard)

    if message.text=='Основы алгоритмов и программирования#':
        sent = bot.send_message(message.chat.id,'Введи задание')
        bot.register_next_step_handler(sent,les1)

    if message.text=='Устройство и функционирование ИС#':
        sent = bot.send_message(message.chat.id,'Введи задние')
        bot.register_next_step_handler(sent,les2)

    if message.text=='Элементы высшей математики#':
        sent = bot.send_message(message.chat.id,'Введи задние')
        bot.register_next_step_handler(sent,les3)

    if message.text=='Русский язык и культура речи#':
        sent = bot.send_message(message.chat.id,'Введи задние')
        bot.register_next_step_handler(sent,les4)

    if message.text=='Инглишь#':
        sent = bot.send_message(message.chat.id,'Введи задние')
        bot.register_next_step_handler(sent,les5)

    if message.text=='Физра#':
        sent = bot.send_message(message.chat.id,'Введи задние')
        bot.register_next_step_handler(sent,les6)

    if message.text=='МДК#':
        sent = bot.send_message(message.chat.id,'Введи задние')
        bot.register_next_step_handler(sent,les7)

    if message.text=='БЖ#':
        sent = bot.send_message(message.chat.id,'Введи задние')
        bot.register_next_step_handler(sent,les8)


    if message.text=='Чг':
        sent = bot.send_message(message.chat.id,'Введи изменения')
        bot.register_next_step_handler(sent,change1)

    if message.text=='Изменения':
        bot.send_message(message.chat.id,database.change)

def les1(message):
    database.les1=message.text
    return database.les1

def les2(message):
    database.les2=message.text
    return database.les2

def les3(message):
    database.les3=message.text
    return database.les3

def les4(message):
    database.les4=message.text
    return database.les4

def les5(message):
    database.les5=message.text
    return database.les5

def les6(message):
    database.les6=message.text
    return database.les6

def les7(message):
    database.les7=message.text
    return database.les7

def les8(message):
    database.les8=message.text
    return database.les8

def mon1(message):
    database.mon1=message.text
    return database.mon1

def tues1(message):
    database.tues1=message.text
    return database.tues1

def wed1(message):
    database.wed1=message.text
    return database.wed1

def thurs1(message):
    database.thurs1=message.text
    return database.thurs1

def wed1(message):
    database.wed1=message.text
    return database.wed1

def fri1(message):
    database.fri1=message.text
    return database.fri1

def sat1(message):
    database.sat1 =message.text
    return database.sat1 



def mon2(message):
    database.mon1=message.text
    return database.mon2

def tues2(message):
    database.tues1=message.text
    return database.tues2

def wed2(message):
    database.wed1=message.text
    return database.wed2

def thurs2(message):
    database.thurs1=message.text
    return database.thurs2

def wed2(message):
    database.wed1=message.text
    return database.wed2

def fri2(message):
    database.fri1=message.text
    return database.fri2

def sat2(message):
    database.sat1 =message.text
    return database.sat2

def chet1(message):
    database.chet =message.text
    return database.chet

def change1(message):
    database.change=message.text
    return database.change
bot.polling()