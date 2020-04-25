import telebot
import time
from dictionary import greetings, description
from telebot import types

bot = telebot.TeleBot("1186945702:AAHUr05kFwHQsPHuaD5CWT3AFfEz4186F9I")

user_dict = {}

class User:
	def __init__(self, name):
		self.name = name
		self.age = None

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, greetings[0])
	msg = bot.send_message(message.chat.id, greetings[1])
	bot.register_next_step_handler(msg, getting_info)

def getting_info(message):
	try:
		chat_id = message.chat.id
		name = message.text
		user = User(name)
		user_dict[chat_id] = user
		msg = bot.send_message(message.chat.id, greetings[2]  + user.name + ":)" + "\n" +
			description[0] + "\n" + description[1] + "\n" + description[2])
		#bot.register_next_step_handler(msg, hello_message)
	except Exception as e:
		bot.reply_to(message, 'oooops')

def ask_about_mood(message):
	bot.send_message(message.chat.id, "How")

def ask_about_mood(message):
	bot.send_message(message.chat.id, "letter")




bot.enable_save_next_step_handlers()	

bot.load_next_step_handlers()

bot.polling(none_stop = True)