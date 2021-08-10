import telebot
from botUtils import *
from user import User
import ssh
from messages import messages

user = User(bot)

@bot.message_handler(commands=["start"])
def tutorial(msg):
    bot.send_message(user.data["chat_id"], messages["start"])
    help(msg)
    
@bot.message_handler(commands=["help"])
def help(msg):
    bot.send_message(user.data["chat_id"], messages["help"])

@bot.message_handler(commands=['on'])
def on(msg):
    global user
    if user.isLogged:
        bot.send_message(user.data["chat_id"], f"{messages['user_already_logged_in']}")
    else: 
        user, user.order = initialize(msg, user)
        if user.order == 0:
            ######## LOGIN ########
            bot.send_message(user.data["chat_id"], messages["login_routine"])
            bot.send_message(user.data["chat_id"], messages["hostname_prompt_login"])
            bot.register_next_step_handler(msg, user.get_hostname)
        elif user.order == 1:
            ######## SIGNUP ########
            bot.send_message(user.data["chat_id"], messages["signup_routine"])
            bot.send_message(user.data["chat_id"], messages["hostname_prompt_signup"])
            bot.register_next_step_handler(msg, user.get_hostname)

@bot.message_handler(commands=["logout"])
def logout(msg):
    user.logout(msg)

@bot.message_handler(commands=["connect"])
def connect(msg):
    # Asking dest and local addresses to connect to
    pass

bot.polling()