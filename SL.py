import telebot
import database


bot = telebot.TeleBot('945462714:AAH0ikBMSiiiwjDBOafR_ZA_5D_o_jW_cPo')


Keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
Keyboard.row('Понедельник','Вторник')
Keyboard.row('Среда','Четверг')
Keyboard.row('Пятница','Субота')
	

@bot.message_handler(content_types = ['text'])
def main(message):
	
	
	if message.text == '/start':
		bot.send_message(message.from_user.id,'На какой день недели рассписание тебе нужно?', reply_markup = Keyboard)


	if message.text == 'Четн':
		sent = bot.send_message(message.chat.id,'Введи чётность')
		bot.register_next_step_handler(sent, chet)

	if database.chet == 'Нечет': week = 1
	else: week = 0


	if message.text == 'Понедельник':
		bot.send_message(message.chat.id,database.mon[week])

	if message.text == 'Вторник':
		bot.send_message(message.chat.id,database.tues[week])

	if message.text == 'Среда':
		bot.send_message(message.chat.id,database.wed[week])

	if message.text == 'Четверг':
		bot.send_message(message.chat.id,database.thurs[week])

	if message.text == 'Пятница':
		bot.send_message(message.chat.id,database.fri[week])

	if message.text == 'Субота':
		bot.send_message(message.chat.id,database.sat[week])


	if message.text == 'Чнг':
		sent = bot.send_message(message.chat.id,'Введи изменения')
		bot.register_next_step_handler(sent,change1)

	if database.change != 'Нет':
		bot.send_message(message.chat.id, 'Изменения:\n' + database.change)


def chet(message):
	database.chet = message.text
	return database.chet

def change1(message):
	database.change = message.text
	return database.change

bot.polling()
