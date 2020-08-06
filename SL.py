#-*- SkorixBOT -*-

import telebot
import shelve
global menu

menu = telebot.types.ReplyKeyboardMarkup(True, False)
menu.row('Понедельник','Вторник')
menu.row('Среда','Четверг')
menu.row('Пятница','Субота')

bot = telebot.TeleBot('945462714:AAH0ikBMSiiiwjDBOafR_ZA_5D_o_jW_cPo')

@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.from_user.id, 'Этот телеграм бот может:\n\n— Показывать рассписание, в зависимости от текущей чётности недели\n\n— Показать актуальное домашнее задание (для этого нужно во просмотра рассписания на какой-либо день недели нажать на интересующий предмет)\n\n— Подсказать имя преподователя (для этого нужно нажать на кнопку слева от интересующего предмета на которой показан кабинет и время начала и окончания занятия)')
    bot.send_message(message.from_user.id, 'На какой день недели тебе нужно рассписание?', reply_markup = menu)

@bot.message_handler(content_types=['text'])

def main(message):

#db
    db = shelve.open('db')
    chet = db['chet']
    change = db['change']
    day = db['day']

#Чётность
    if message.text=='Четн':
        Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
        Keyboard.row('ЧЁТНАЯ', 'НЕЧЁТНАЯ')
        Keyboard.row('НАЗАД')
        msg = bot.send_message(message.chat.id, f'Сейчас {chet} неделя', reply_markup = Keyboard)
        bot.register_next_step_handler(msg, chetn)

#Рассписание
    RaspisanieZvonkov = 'Рассписание звонков\n1:   8:30 - 10:05\n2: 10:25 - 12:00\n3: 12:30 - 14:05\n4: 14:15 - 15:50\n5: 16:00 - 17:35\n6: 17:45 - 19:25\n7: 19:25 - 21:00'

    if message.text == 'Понедельник':
        if chet == 'ЧЁТНАЯ':
            Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
            Keyboard.row('НАЗАД')
            Keyboard.row(' 8:30 - 10:05\n23', 'Элементы высшей математики')
            Keyboard.row('10:25 - 12:00\n301/2', 'МДК')
            Keyboard.row('12:30 - 14:05\n310/3', 'Устройство и функционирование ИС')
            bot.send_message(message.from_user.id, RaspisanieZvonkov, reply_markup = Keyboard)
        else:
            Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
            Keyboard.row('НАЗАД')
            Keyboard.row(' 8:30 - 10:05\n317', 'Элементы высшей математики')
            Keyboard.row('10:25 - 12:00\n316', 'МДК')
            Keyboard.row('12:30 - 14:05\n301/2', 'Устройство и функционирование ИС')
            bot.send_message(message.from_user.id, RaspisanieZvonkov, reply_markup = Keyboard)
        if change != 'Нет' and day == 'Понедельник':
            bot.send_message(message.chat.id, f'Изменения:\n{change}')

    if message.text == 'Вторник':
        if chet == 'ЧЁТНАЯ':
            Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
            Keyboard.row('НАЗАД')
            Keyboard.row(' 8:30 - 10:05\n113', 'Основы алгоритмизации и программирования')
            Keyboard.row('10:25 - 12:00\n401', 'Физра')
            Keyboard.row('12:30 - 14:05\n22', 'Элементы высшей математики')
            bot.send_message(message.from_user.id, RaspisanieZvonkov, reply_markup = Keyboard)
        else:
            Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
            Keyboard.row('НАЗАД')
            Keyboard.row(' 8:30 - 10:05\n301/3', 'Основы алгоритмизации и программирования')
            Keyboard.row('10:25 - 12:00\n301/2', 'МДК')
            Keyboard.row('12:30 - 14:05\n316', 'Элементы высшей математики')
            bot.send_message(message.from_user.id, RaspisanieZvonkov, reply_markup = Keyboard)
        if change != 'Нет' and day == 'Вторник':
            bot.send_message(message.chat.id, f'Изменения:\n{change}')

    if message.text == 'Среда':
        if chet == 'ЧЁТНАЯ':
            Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
            Keyboard.row('НАЗАД')
            Keyboard.row(' 8:30 - 10:05\n301/2', 'Устройство и функционирование ИС')
            Keyboard.row('10:25 - 12:00\n401', 'Физра')
            Keyboard.row('12:30 - 14:05\n22', 'Элементы высшей математики')
            bot.send_message(message.from_user.id, RaspisanieZvonkov, reply_markup = Keyboard)
        else:
            Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
            Keyboard.row('НАЗАД')
            Keyboard.row(' 8:30 - 10:05\n301/2', 'Устройство и функционирование ИС')
            Keyboard.row('10:25 - 12:00\n401', 'Физра')
            Keyboard.row('12:30 - 14:05\n316', 'Элементы высшей математики')
            bot.send_message(message.from_user.id, RaspisanieZvonkov, reply_markup = Keyboard)
        if change != 'Нет' and day == 'Среда':
            bot.send_message(message.chat.id, RaspisanieZvonkov)
            bot.send_message(message.chat.id, f'Изменения:\n{change}')


    if message.text == 'Четверг':
        if chet == 'ЧЁТНАЯ':
            Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
            Keyboard.row('НАЗАД')
            Keyboard.row(' 8:30 - 10:05\nНет', 'МДК')
            Keyboard.row('10:25 - 12:00\n107/5', 'Инглишь')
            Keyboard.row('12:30 - 14:05\n309', 'Русский язык и культура речи')
            bot.send_message(message.from_user.id, RaspisanieZvonkov, reply_markup = Keyboard)
        else:
            Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
            Keyboard.row('НАЗАД')
            Keyboard.row(' 8:30 - 10:05\n11', 'ДК')
            Keyboard.row('10:25 - 12:00\n107/5', 'Инглишь')
            Keyboard.row('12:30 - 14:05\n113', 'Основы алгоритмизации и программирования')
            bot.send_message(message.from_user.id, RaspisanieZvonkov, reply_markup = Keyboard)
        if change != 'Нет' and day == 'Четверг':
            bot.send_message(message.chat.id, RaspisanieZvonkov)
            bot.send_message(message.chat.id, f'Изменения:\n{change}')

    if message.text == 'Пятница':
        if chet == 'ЧЁТНАЯ':
            Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
            Keyboard.row('НАЗАД')
            Keyboard.row(' 8:30 - 10:05\nНет', 'Элементы высшей математики')
            Keyboard.row('10:25 - 12:00\nНет', 'БЖ')
            Keyboard.row('12:30 - 14:05\nНет', 'Устройство и функционирование ИС')
            bot.send_message(message.from_user.id, RaspisanieZvonkov, reply_markup = Keyboard)
        else:
            Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
            Keyboard.row('НАЗАД')
            Keyboard.row(' 8:30 - 10:05\n310', 'Элементы высшей математики')
            Keyboard.row('10:25 - 12:00\n407', 'БЖ')
            Keyboard.row('12:30 - 14:05\n412', 'Устройство и функционирование ИС')
            bot.send_message(message.from_user.id, RaspisanieZvonkov, reply_markup = Keyboard)
        if change != 'Нет' and day == 'Пятница':
            bot.send_message(message.chat.id, RaspisanieZvonkov)
            bot.send_message(message.chat.id, f'Изменения:\n{change}')

    if message.text == 'Субота':
        chet = db['chet']
        day = db['day']
        change = db['change']
        if chet == 'ЧЁТНАЯ':
            Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
            Keyboard.row('НАЗАД')
            Keyboard.row(' 8:30 - 10:05\n113', 'Основы алгоритмизации и программирования')
            Keyboard.row('10:25 - 12:00\n309', 'Русский язык и культура речи')
            Keyboard.row('12:30 - 14:05\nНет', 'МДК')
            bot.send_message(message.from_user.id, RaspisanieZvonkov, reply_markup = Keyboard)
        else:
            Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
            Keyboard.row('НАЗАД')
            Keyboard.row(' 8:30 - 10:05\n113', 'Основы алгоритмизации и программирования')
            Keyboard.row('10:25 - 12:00\n309', 'Русский язык и культура речи')
            Keyboard.row('12:30 - 14:05\n301/2', 'МДК')
            bot.send_message(message.from_user.id, RaspisanieZvonkov, reply_markup = Keyboard)
        if change != 'Нет' and day == 'Субота':
            bot.send_message(message.chat.id, RaspisanieZvonkov)
            bot.send_message(message.chat.id, f'Изменения:\n{change}')

    if message.text == 'Инглишь':
        Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
        Keyboard.row('Кайфеджан','Тихонова')
        bot.send_message(message.chat.id, 'Какой группы?', reply_markup = Keyboard)

#Изменения
    if message.text == 'Чнг':
        Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
        Keyboard.row('Изменений нет')
        Keyboard.row('Понедельник','Вторник')
        Keyboard.row('Среда','Четверг')
        Keyboard.row('Пятница','Субота')
        sent = bot.send_message(message.chat.id, 'На какой день недели изменения?', reply_markup = Keyboard)
        bot.register_next_step_handler(sent, dayt)

#ДЗ
    if message.text == 'Дз':
        Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
        Keyboard.row('НАЗАД')
        Keyboard.row('Основы алгоритмов и программирования#')
        Keyboard.row('Устройство и функционирование ИС#')
        Keyboard.row('Элементы высшей математики#')
        Keyboard.row('Русский язык и культура речи#')
        Keyboard.row('Инглишь#')
        Keyboard.row('МДК#')
        Keyboard.row('БЖ#')
        bot.send_message(message.chat.id, 'На какой предмет?', reply_markup = Keyboard)

    if message.text == 'Основы алгоритмов и программирования#':
        sent = bot.send_message(message.chat.id,'Введи задание')
        bot.register_next_step_handler(sent, les1)

    if message.text == 'Устройство и функционирование ИС#':
        sent = bot.send_message(message.chat.id,'Введи задание')
        bot.register_next_step_handler(sent, les2)

    if message.text == 'Элементы высшей математики#':
        sent = bot.send_message(message.chat.id,'Введи задание')
        bot.register_next_step_handler(sent, les3)

    if message.text == 'Русский язык и культура речи#':
        sent = bot.send_message(message.chat.id,'Введи задание')
        bot.register_next_step_handler(sent, les4)

    if message.text == 'МДК#':
        sent = bot.send_message(message.chat.id,'Введи задание')
        bot.register_next_step_handler(sent, les5)

    if message.text == 'БЖ#':
        sent = bot.send_message(message.chat.id,'Введи задание')
        bot.register_next_step_handler(sent, les6)

    if message.text == 'Инглишь#':
        sent = bot.send_message(message.chat.id,'Введи задание')
        bot.register_next_step_handler(sent, les7)

    if message.text == 'Илья':
        sent = bot.send_message(message.chat.id, 'ЯОЙЩИК!!!\n\nВведи задание')
        bot.register_next_step_handler(sent, les8)


    if message.text == 'Основы алгоритмизации и программирования':
        bot.send_message(message.chat.id, db['les1'])

    if message.text == 'Устройство и функционирование ИС':
        bot.send_message(message.chat.id, db['les2'])

    if message.text == 'Элементы высшей математики':
        bot.send_message(message.chat.id, db['les3'])

    if message.text == 'Русский язык и культура речи':
        bot.send_message(message.chat.id, db['les4'])

    if message.text == 'МДК':
        bot.send_message(message.chat.id, db['les5'])

    if message.text == 'БЖ':
        bot.send_message(message.chat.id, db['les6'])

    if message.text == 'Кайфеджан':
        bot.send_message(message.chat.id, db['les7'], reply_markup = menu)

    if message.text == 'Тихонова':
        bot.send_message(message.chat.id, db['les8'], reply_markup = menu)

#ФИО
    if message.text in ['8:30 - 10:05\n23', '12:30 - 14:05\n22', '8:30 - 10:05\nНет', '8:30 - 10:05\n317', '12:30 - 14:05\n316', '8:30 - 10:05\n310']:
        bot.send_message(message.from_user.id, 'Математик')

    if message.text in ['10:25 - 12:00\n301/2', '12:30 - 14:05\nНет', '10:25 - 12:00\n316', '10:25 - 12:00\n316']:
        bot.send_message(message.from_user.id, 'Мясникова')

    if message.text in ['12:30 - 14:05\n310/3', '8:30 - 10:05\n301/2', '12:30 - 14:05\nНет', '12:30 - 14:05\n301/2', '12:30 - 14:05\n412']:
        bot.send_message(message.from_user.id, 'Мыльникова')

    if message.text in ['8:30 - 10:05\n113', '8:30 - 10:05\n301/3', '12:30 - 14:05\n113']:
        bot.send_message(message.from_user.id, 'Паутова')

    if message.text in ['10:25 - 12:00\n401']:
        bot.send_message(message.from_user.id, 'Виктор Борисович')

    if message.text in ['10:25 - 12:00\n107/5']:
        bot.send_message(message.from_user.id, 'Кайфеджан')

    if message.text in ['12:30 - 14:05\n309', '10:25 - 12:00\n309']:
        bot.send_message(message.from_user.id, 'Анджела Арамовна')

    if message.text in ['10:25 - 12:00\nНет', '10:25 - 12:00\n407']:
        bot.send_message(message.from_user.id, 'Габриэлян')

#НАЗАД
    if message.text == 'НАЗАД':
        bot.send_message(message.from_user.id, 'На какой день недели тебе нужно рассписание?', reply_markup = menu)

#СЮРЕАЛИЗАЦИЯ
def chetn(message):
    db = shelve.open('db')
    chet = db['chet']
    if message.text == 'ЧЁТНАЯ':
        db['chet'] = 'ЧЁТНАЯ'
    if message.text == 'НЕЧЁТНАЯ':
        db['chet'] =  'НЕЧЁТНАЯ'
    chet = db['chet']
    bot.send_message(message.chat.id, f'Теперь {chet} неделя', reply_markup = menu)
    db.close()
def change(message):
    db = shelve.open('db')
    db['change'] = message.text
    db.close()
    bot.send_message(message.from_user.id, 'На какой день недели тебе нужно рассписание?', reply_markup = menu)
def dayt(message):
    db = shelve.open('db')
    if message.text == 'Изменений нет':
        db['change'] = 'Нет'
        bot.send_message(message.from_user.id, 'На какой день недели тебе нужно рассписание?', reply_markup = menu)
    else:
        db['day'] = message.text
        sent = bot.send_message(message.chat.id, 'Введи изменения')
        bot.register_next_step_handler(sent, change)
    db.close()
def les1(message):
    db = shelve.open('db')
    db['les1'] = message.text
    db.close()
def les2(message):
    db = shelve.open('db')
    db['les2'] = message.text
    db.close()
def les3(message):
    db = shelve.open('db')
    db['les3'] = message.text
    db.close()
def les4(message):
    db = shelve.open('db')
    db['les4'] = message.text
    db.close()
def les5(message):
    db = shelve.open('db')
    db['les5'] = message.text
    db.close()
def les6(message):
    db = shelve.open('db')
    db['les6'] = message.text
    db.close()
def les7(message):
    db = shelve.open('db')
    db['les7'] = message.text
    db.close()
def les8(message):
    db = shelve.open('db')
    db['les8'] = message.text
    db.close()
bot.polling()