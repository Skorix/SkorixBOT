import telebot
import database


bot = telebot.TeleBot('945462714:AAH0ikBMSiiiwjDBOafR_ZA_5D_o_jW_cPo')
	
   
menu = telebot.types.ReplyKeyboardMarkup(True, False)
menu.row('Понедельник','Вторник')
menu.row('Среда','Четверг')
menu.row('Пятница','Субота')
menu.row('Изменения')


@bot.message_handler(content_types=['text'])
def main(message):
	

	if message.text == '/start':
		bot.send_message(message.from_user.id, 'На какой день недели тебе нужно рассписание?', reply_markup = menu)


	if message.text=='Четн':
		sent = bot.send_message(message.chat.id,'Введи чётность')
		bot.register_next_step_handler(sent, chet)


	if message.text == 'Понедельник' and database.chet == 'Чет':
		Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
		Keyboard.row('23 - Элементы высшей математики')
		Keyboard.row('301/2 - МДК')
		Keyboard.row('310/3 - Устройство и функционирование ИС')
		Keyboard.row('Назад')
		bot.send_message(message.from_user.id, 'Понедельник', reply_markup = Keyboard)

	if message.text == 'Вторник' and database.chet == 'Чет':
		Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
		Keyboard.row('113 - Основы алгоритмизации и программирования')
		Keyboard.row('401 - Физра')
		Keyboard.row('22 - Элементы высшей математики')
		Keyboard.row('Назад')
		bot.send_message(message.from_user.id, 'Вторник', reply_markup = Keyboard)

	if message.text == 'Среда' and database.chet == 'Чет':
		Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
		Keyboard.row('301/2 - Устройство и функционирование ИС')
		Keyboard.row('401 - Физра')
		Keyboard.row('22 - Элементы высшей математики')
		Keyboard.row('Назад')
		bot.send_message(message.from_user.id, 'Среда', reply_markup = Keyboard)

	if message.text == 'Четверг' and database.chet == 'Чет':
		Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
		Keyboard.row('Нет-МДК')
		Keyboard.row('107/5 - Инглишь')
		Keyboard.row('309 - Русский язык и культура речи')
		Keyboard.row('Назад')
		bot.send_message(message.from_user.id, 'Четверг', reply_markup = Keyboard)

	if message.text == 'Пятница' and database.chet == 'Чет':
		Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
		Keyboard.row('Нет - Элементы высшей математики')
		Keyboard.row('Нет - БЖ')
		Keyboard.row('Нет - Устройство и функционирование ИС')
		Keyboard.row('Назад')
		bot.send_message(message.from_user.id, 'Пятница', reply_markup = Keyboard)

	if message.text == 'Субота' and database.chet == 'Чет':
		Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
		Keyboard.row('113 - Основы алгоритмизации и программирования')
		Keyboard.row('309 - Русский язык и культура речи')
		Keyboard.row('Нет - МДК')
		Keyboard.row('Назад')
		bot.send_message(message.from_user.id, 'Субота', reply_markup = Keyboard)


	if message.text == 'Понедельник' and database.chet == 'Нечет':
		Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
		Keyboard.row('317 - Элементы высшей математики')
		Keyboard.row('316 - МДК')
		Keyboard.row('301/2 - Устройство и функционирование ИС')
		Keyboard.row('Назад')
		bot.send_message(message.from_user.id, 'Понедельник', reply_markup = Keyboard)

	if message.text == 'Вторник' and database.chet == 'Нечет':
		Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
		Keyboard.row('301/3 - Основы алгоритмизации и программирования')
		Keyboard.row('301/2 - МДК')
		Keyboard.row('316 - Элементы высшей математики')
		Keyboard.row('Назад')
		bot.send_message(message.from_user.id, 'Вторник', reply_markup = Keyboard)

	if message.text == 'Среда' and database.chet == 'Нечет':
		Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
		Keyboard.row('301/2 - Устройство и функционирование ИС')
		Keyboard.row('401 - Физра')
		Keyboard.row('316 - Элементы высшей математики')
		Keyboard.row('Назад')
		bot.send_message(message.from_user.id, 'Среда', reply_markup = Keyboard)

	if message.text == 'Четверг' and database.chet == 'Нечет':
		Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
		Keyboard.row('113-МДК')
		Keyboard.row('107/5 - Инглишь')
		Keyboard.row('113 - Основы алгоритмизации и программирования')
		Keyboard.row('Назад')
		bot.send_message(message.from_user.id, 'Четверг', reply_markup = Keyboard)

	if message.text == 'Пятница' and database.chet == 'Нечет':
		Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
		Keyboard.row('310 - Элементы высшей математики')
		Keyboard.row('407 - БЖ')
		Keyboard.row('412 - Устройство и функционирование ИС')
		Keyboard.row('Назад')
		bot.send_message(message.from_user.id, 'Пятница', reply_markup = Keyboard)

	if message.text == 'Субота' and database.chet == 'Нечет':
		Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
		Keyboard.row('113 - Основы алгоритмизации и программирования')
		Keyboard.row('309 - Русский язык и культура речи')
		Keyboard.row('301/2 - МДК')
		Keyboard.row('Назад')
		bot.send_message(message.from_user.id, 'Субота', reply_markup = Keyboard)

	if message.text == '107/5 - Инглишь':
		Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
		Keyboard.row('Кайфеджан','Тихонова')
		Keyboard.row('Назад')
		bot.send_message(message.chat.id, 'Какой группы?', reply_markup = Keyboard)


		global DZ_NUM
		DZ_NUM = 0

	if message.text == '113 - Основы алгоритмизации и программирования' and '301/3 - Основы алгоритмизации и программирования':
		DZ_NUM = 0
		bot.send_message(message.chat.id,database.lesson[DZ_NUM])

	if message.text == '310/3 - Устройство и функционирование ИС' and '301/2 - Устройство и функционирование ИС' and '412 - Устройство и функционирование ИС':
		DZ_NUM = 1
		bot.send_message(message.chat.id,database.lesson[DZ_NUM]) 

	if message.text == '23 - Элементы высшей математики' and '22 - Элементы высшей математики' and 'Нет - Элементы высшей математики' and '317 - Элементы высшей математики' and '316 - Элементы высшей математики' and '310 - Элементы высшей математики':
		DZ_NUM = 2
		bot.send_message(message.chat.id,database.lesson[DZ_NUM])

	if message.text == '309 - Русский язык и культура речи':
		DZ_NUM = 3
		bot.send_message(message.chat.id,database.lesson[DZ_NUM])

	if message.text == '301/2 - МДК' and 'Нет-МДК' and '316 - МДК' and '113-МДК':
		DZ_NUM = 4
		bot.send_message(message.chat.id,database.lesson[DZ_NUM])

	if message.text == 'Нет - БЖ' and '407 - БЖ':
		DZ_NUM = 5
		bot.send_message(message.chat.id,database.lesson[DZ_NUM])

	if message.text == 'Кайфеджан':
		DZ_NUM = 6
		bot.send_message(message.chat.id,database.lesson[DZ_NUM])

	if message.text == 'Тихонова':
		DZ_NUM = 7
		bot.send_message(message.chat.id,database.lesson[DZ_NUM])


	if message.text == 'Админ на месте':
		Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
		Keyboard.row('Основы алгоритмов и программирования#')
		Keyboard.row('Устройство и функционирование ИС#')
		Keyboard.row('Элементы высшей математики#')
		Keyboard.row('Русский язык и культура речи#')
		Keyboard.row('Инглишь#')
		Keyboard.row('МДК#')
		Keyboard.row('БЖ#')
		Keyboard.row('Назад')
		bot.send_message(message.chat.id, 'На какой предмет?', reply_markup = Keyboard)

	if message.text == 'Основы алгоритмов и программирования#':
		DZ_NUM = 0
		sent = bot.send_message(message.chat.id,'Введи задание')
		bot.register_next_step_handler(sent, lesson)

	if message.text == 'Устройство и функционирование ИС#':
		DZ_NUM = 1
		sent = bot.send_message(message.chat.id,'Введи задание')
		bot.register_next_step_handler(sent, lesson)

	if message.text == 'Элементы высшей математики#':
		DZ_NUM = 2
		sent = bot.send_message(message.chat.id,'Введи задание')
		bot.register_next_step_handler(sent, lesson)

	if message.text == 'Русский язык и культура речи#':
		DZ_NUM = 3
		sent = bot.send_message(message.chat.id,'Введи задание')
		bot.register_next_step_handler(sent, lesson)

	if message.text == 'МДК#':
		DZ_NUM = 4
		sent = bot.send_message(message.chat.id,'Введи задание')
		bot.register_next_step_handler(sent, lesson)

	if message.text == 'БЖ#':
		DZ_NUM = 5
		sent = bot.send_message(message.chat.id,'Введи задание')
		bot.register_next_step_handler(sent, lesson)

	if message.text == 'Инглишь':
		DZ_NUM = 6
		sent = bot.send_message(message.chat.id,'Введи задание')
		bot.register_next_step_handler(sent, lesson)

	if message.text == 'Илья яойщик':
		DZ_NUM = 7
		sent = bot.send_message(message.chat.id,'Введи задание')
		bot.register_next_step_handler(sent, lesson)


	if message.text == 'Назад':
		bot.send_message(message.from_user.id, 'На какой день недели тебе нужно рассписание?', reply_markup = menu)


	if message.text == 'Чнг':
		sent = bot.send_message(message.chat.id,'Введи изменения')
		bot.register_next_step_handler(sent,change1)

	if message.text == 'Изменения':
		bot.send_message(message.chat.id,database.change)


def chet(message):
	database.chet = message.text
	return database.chet

def lesson(message):
	database.lesson[DZ_NUM] = message.text
	return database.lesson[DZ_NUM]

def change1(message):
	database.change = message.text
	return database.change

bot.polling()