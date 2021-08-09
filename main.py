import telebot
from botUtils import *
from user import User
import ssh

user = User(bot)
order = None

@bot.message_handler(commands=["connect"])
def show_menu(message):
    bot.reply_to(message, "Connecting to Atlas...")

@bot.message_handler(commands=['on'])
def on(msg):
    global user, order
    if user.isLogged:
        bot.send_message(user.data["chat_id"], f"No hace falta que vuelvas a identificarte, {user.data['username']}")
    else: 
        user, order = initialize(msg, user)
        if order == 0:
            ######## LOGIN ########
            bot.send_message(user.data["chat_id"], "Iniciando rutina de log in")
            bot.send_message(user.data["chat_id"], "Introduce tu nombre de usuario")
            bot.register_next_step_handler(msg, user.get_hostname)
        elif order == 1:
            ######## SIGNUP ########
            bot.send_message(user.data["chat_id"], "Iniciando rutina de registro")
            bot.send_message(user.data["chat_id"], "Elige tu nombre de usuario")
            bot.register_next_step_handler(msg, user.get_hostname)

@bot.message_handler(commands=["connect"])
def connect(msg):
    # Asking dest and local addresses to connect to
    pass

bot.polling()