import telebot
from botUtils import bot, cluster_msg, connect_to_cluster, exec_login

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=["connect"])
def show_menu(message):
    bot.reply_to(message, cluster_msg)

@bot.message_handler(func=lambda message: message.text in ["1", "2", "3"])
def process_message(message):
	#connect_to_cluster(int(message.text))
	pass

@bot.message_handler(commands=["on"])
def login(msg):
    	exec_login(msg)

bot.polling()