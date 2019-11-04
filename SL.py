#-*- SLBOT -*-
import telebot
import shelve
global menu

bot = telebot.TeleBot('857593648:AAFR6ED50U5I5id5d4KWlLMhVTxHE1uKVPU')

@bot.message_handler(content_types=['text'])
def main(message):
#start
	menu = telebot.types.ReplyKeyboardMarkup(True, False)
	menu.row('Понедельник','Вторник')
	menu.row('Среда','Четверг')
	menu.row('Пятница','Субота')
	msg = bot.send_message(message.from_user.id, 'На какой день недели тебе нужно рассписание?', reply_markup = menu)
	bot.register_next_step_handler(msg, main)
#Чётность
	if message.text=='Четн':
		db = shelve.open('db')
		chet = db['chet']
		Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
		Keyboard.row('ЧЁТНАЯ', 'НЕЧЁТНАЯ')
		Keyboard.row('НАЗАД')
		msg = bot.send_message(message.chat.id, f'Сейчас {chet} неделя', reply_markup = Keyboard)
		bot.register_next_step_handler(msg, chetn)
		db.close()
#Рассписание
	if message.text == 'Понедельник':
		db = shelve.open('db')
		chet = db['chet']
		day = db['day']
		change = db['change']
		db.close()
		if chet == 'ЧЁТНАЯ':
			Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
			Keyboard.row('НАЗАД')
			Keyboard.row('23', 'Элементы высшей математики')
			Keyboard.row('301/2', 'МДК')
			Keyboard.row('310/3', 'Устройство и функционирование ИС')
			bot.send_message(message.from_user.id, 'Понедельник', reply_markup = Keyboard)
			if change != 'Нет':
				if day == 'Понедельник':
					bot.send_message(message.chat.id, 'Изменения:\n' + change)

	if message.text == 'Вторник':
		db = shelve.open('db')
		chet = db['chet']
		day = db['day']
		change = db['change']
		db.close()
		if chet == 'ЧЁТНАЯ':
			Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
			Keyboard.row('НАЗАД')
			Keyboard.row('113', 'Основы алгоритмизации и программирования')
			Keyboard.row('401', 'Физра')
			Keyboard.row('22', 'Элементы высшей математики')
			bot.send_message(message.from_user.id, 'Вторник', reply_markup = Keyboard)
			if change != 'Нет':
				if day == 'Вторник':
					bot.send_message(message.chat.id, 'Изменения:\n' + change)

	if message.text == 'Среда':
		db = shelve.open('db')
		chet = db['chet']
		day = db['day']
		change = db['change']
		db.close()
		if chet == 'ЧЁТНАЯ':
			Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
			Keyboard.row('НАЗАД')
			Keyboard.row('301/2', 'Устройство и функционирование ИС')
			Keyboard.row('401', 'Физра')
			Keyboard.row('22', 'Элементы высшей математики')
			bot.send_message(message.from_user.id, 'Среда', reply_markup = Keyboard)
			if change != 'Нет':
				if day == 'Среда':
					bot.send_message(message.chat.id, 'Изменения:\n' + change)

	if message.text == 'Четверг':
		db = shelve.open('db')
		chet = db['chet']
		day = db['day']
		change = db['change']
		db.close()
		if chet == 'ЧЁТНАЯ':
			Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
			Keyboard.row('НАЗАД')
			Keyboard.row('Не', 'ДК')
			Keyboard.row('107/5', 'Инглишь')
			Keyboard.row('309', 'Русский язык и культура речи')
			bot.send_message(message.from_user.id, 'Четверг', reply_markup = Keyboard)
			if change != 'Нет':
				if day == 'Четверг':
					bot.send_message(message.chat.id, 'Изменения:\n' + change)

	if message.text == 'Пятница':
		db = shelve.open('db')
		chet = db['chet']
		day = db['day']
		change = db['change']
		db.close()
		if chet == 'ЧЁТНАЯ':
			Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
			Keyboard.row('НАЗАД')
			Keyboard.row('Нет', 'Элементы высшей математики')
			Keyboard.row('Нет', 'БЖ')
			Keyboard.row('Нет', 'Устройство и функционирование ИС')
			bot.send_message(message.from_user.id, 'Пятница', reply_markup = Keyboard)
			if change != 'Нет':
				if day == 'Пятница':
					bot.send_message(message.chat.id, 'Изменения:\n' + change)

	if message.text == 'Субота':
		db = shelve.open('db')
		chet = db['chet']
		day = db['day']
		change = db['change']
		db.close()
		if chet == 'ЧЁТНАЯ':
			Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
			Keyboard.row('НАЗАД')
			Keyboard.row('113', 'Основы алгоритмизации и программирования')
			Keyboard.row('309', 'Русский язык и культура речи')
			Keyboard.row('Нет', 'МДК')
			bot.send_message(message.from_user.id, 'Субота', reply_markup = Keyboard)
			if change != 'Нет':
				if day == 'Субота':
					bot.send_message(message.chat.id, 'Изменения:\n' + change)


	if message.text == 'Понедельник':
		db = shelve.open('db')
		chet = db['chet']
		day = db['day']
		change = db['change']
		db.close()
		if chet == 'НЕЧЁТНАЯ':
			Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
			Keyboard.row('НАЗАД')
			Keyboard.row('317', 'Элементы высшей математики')
			Keyboard.row('316', 'МДК')
			Keyboard.row('301/2', 'Устройство и функционирование ИС')
			bot.send_message(message.from_user.id, 'Понедельник', reply_markup = Keyboard)
			if change != 'Нет':
				if day == 'Понедельник':
					bot.send_message(message.chat.id, 'Изменения:\n' + change)

	if message.text == 'Вторник':
		db = shelve.open('db')
		chet = db['chet']
		day = db['day']
		change = db['change']
		db.close()
		if chet == 'НЕЧЁТНАЯ':
			Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
			Keyboard.row('НАЗАД')
			Keyboard.row('301/3', 'Основы алгоритмизации и программирования')
			Keyboard.row('301/2', 'МДК')
			Keyboard.row('316', 'Элементы высшей математики')
			bot.send_message(message.from_user.id, 'Вторник', reply_markup = Keyboard)
			if change != 'Нет':
				if day == 'Вторник':
					bot.send_message(message.chat.id, 'Изменения:\n' + change)

	if message.text == 'Среда':
		db = shelve.open('db')
		chet = db['chet']
		day = db['day']
		change = db['change']
		db.close()
		if chet == 'НЕЧЁТНАЯ':
			Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
			Keyboard.row('НАЗАД')
			Keyboard.row('301/2', 'Устройство и функционирование ИС')
			Keyboard.row('401', 'Физра')
			Keyboard.row('316', 'Элементы высшей математики')
			bot.send_message(message.from_user.id, 'Среда', reply_markup = Keyboard)
			if change != 'Нет':
				if day == 'Среда':
					bot.send_message(message.chat.id, 'Изменения:\n' + change)

	if message.text == 'Четверг':
		db = shelve.open('db')
		chet = db['chet']
		day = db['day']
		change = db['change']
		db.close()
		if chet == 'НЕЧЁТНАЯ':
			Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
			Keyboard.row('НАЗАД')
			Keyboard.row('11', 'ДК')
			Keyboard.row('107/5', 'Инглишь')
			Keyboard.row('113', 'Основы алгоритмизации и программирования')
			bot.send_message(message.from_user.id, 'Четверг', reply_markup = Keyboard)
			if change != 'Нет':
				if day == 'Четверг':
					bot.send_message(message.chat.id, 'Изменения:\n' + change)

	if message.text == 'Пятница':
		db = shelve.open('db')
		chet = db['chet']
		day = db['day']
		change = db['change']
		db.close()
		if chet == 'НЕЧЁТНАЯ':
			Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
			Keyboard.row('НАЗАД')
			Keyboard.row('310', 'Элементы высшей математики')
			Keyboard.row('407', 'БЖ')
			Keyboard.row('412', 'Устройство и функционирование ИС')
			bot.send_message(message.from_user.id, 'Пятница', reply_markup = Keyboard)
			if change != 'Нет':
				if day == 'Пятница':
					bot.send_message(message.chat.id, 'Изменения:\n' + change)

	if message.text == 'Субота':
		db = shelve.open('db')
		chet = db['chet']
		day = db['day']
		change = db['change']
		db.close()
		if chet == 'НЕЧЁТНАЯ':
			Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
			Keyboard.row('НАЗАД')
			Keyboard.row('113', 'Основы алгоритмизации и программирования')
			Keyboard.row('309', 'Русский язык и культура речи')
			Keyboard.row('301/2', 'МДК')
			bot.send_message(message.from_user.id, 'Субота', reply_markup = Keyboard)
			if change != 'Нет':
				if day == 'Субота':
					bot.send_message(message.chat.id, 'Изменения:\n' + change)

	if message.text == 'Инглишь':
		Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
		Keyboard.row('Кайфеджан','Тихонова')
		Keyboard.row('НАЗАД')
		bot.send_message(message.chat.id, 'Какой группы?', reply_markup = Keyboard)
#Изменения
	if message.text == 'Нет':
		db = shelve.open('db')
		db['change'] = 'Нет'
		db.close()

	if message.text == 'Чнг':
		Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
		Keyboard.row('Понедельник','Вторник')
		Keyboard.row('Среда','Четверг')
		Keyboard.row('Пятница','Субота')
		sent = bot.send_message(message.chat.id, 'На какой день недели изменения?', reply_markup = Keyboard)
		bot.register_next_step_handler(sent, dayt)
#ДЗ
	if message.text == 'Дз':
		Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
		Keyboard.row('Основы алгоритмов и программирования#')
		Keyboard.row('Устройство и функционирование ИС#')
		Keyboard.row('Элементы высшей математики#')
		Keyboard.row('Русский язык и культура речи#')
		Keyboard.row('Инглишь#')
		Keyboard.row('МДК#')
		Keyboard.row('БЖ#')
		Keyboard.row('НАЗАД')
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


	db = shelve.open('db')
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
		bot.send_message(message.chat.id, db['les7'])

	if message.text == 'Тихонова':
		bot.send_message(message.chat.id, db['les8'])
	db.close()
#НАЗАД
	if message.text == 'НАЗАД':
		menu = telebot.types.ReplyKeyboardMarkup(True, False)
		menu.row('Понедельник','Вторник')
		menu.row('Среда','Четверг')
		menu.row('Пятница','Субота')
		bot.send_message(message.from_user.id, 'На какой день недели тебе нужно рассписание?', reply_markup = menu)
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
def dayt(message):
	db = shelve.open('db')
	db['day'] = message.text
	db.close()
	sent = bot.send_message(message.chat.id, 'Введи изменения')
	bot.register_next_step_handler(sent, change)
def change(message):
	db = shelve.open('db')
	db['change'] = message.text
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