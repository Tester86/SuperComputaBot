import telebot
from botUtils import *
from user import User
from db import db

user = User()
order = None

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

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
            bot.send_message(user.data["chat_id"], "Iniciando rutina de log in")
            bot.send_message(user.data["chat_id"], "Introduce tu nombre de usuario")
        elif order == 1:
            bot.send_message(user.data["chat_id"], "Iniciando rutina de registro")
            bot.send_message(user.data["chat_id"], "Elige tu nombre de usuario")


@bot.message_handler()
def unknown(msg):
    global user, order
    db_obj = db()
    db_data = db_obj.get_data()
    if order == 0:
        ####### LOGIN PROCESS #######
        if not user.isLogged:
            if user.state == user.ASKING_USERNAME:
                user.data["username"] = msg.text
                user.state = user.ASKING_PASSWORD
                bot.send_message(msg.chat.id, "Introduce tu contraseña")
            elif user.state == user.ASKING_PASSWORD:
                user.data["password"] = msg.text
                if(user.authenticate()):
                    user.isLogged = True
                    bot.send_message(user.data["chat_id"], "Log in completado con éxito")
                else:
                    bot.send_message(user.data["chat_id"], "Nombre de usuario o contraseña incorrectos, pruebe otra vez")
    elif order == 1:
        ####### SIGNUP PROCESS #######
        if not user.isLogged:
            if user.state == user.ASKING_USERNAME:
                for i in db_data:
                    if i["username"] == msg.text:
                        bot.send_message(user.data["chat_id"], "Lo siento, este nombre de usuario no está disponible, prueba con otro")
                        unknown(msg) # CAUTION: PROBABLY WRONG
                    else:
                        user.data["username"] = msg.text
                        user.state = user.ASKING_PASSWORD
                        bot.send_message(user.data["chat_id"], "Elige tu contraseña")
            elif user.state == user.ASKING_PASSWORD:
                user.data["password"] = msg.text
                db_obj.insert_user(user.data)
                bot.send_message(user.data["chat_id"], "Usuario registrado con éxito")
                user.isLogged = True
            
                        

bot.polling()