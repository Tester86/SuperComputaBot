from threading import Timer
import pymongo
from db import db
from messages import messages

class User:
    def __init__(self, bot):
        self.bot = bot
        self.data = {"hostname" : None, "password": None, "chat_id": None}
        self.isLogged = False
        self.order = None
    def get_hostname(self, msg):
        self.data["hostname"] = msg.text
        self.bot.send_message(self.data["chat_id"], "Contraseña")
        self.bot.register_next_step_handler(msg, self.get_password)
    def get_password(self, msg):
        self.data["password"] = msg.text
        if self.order == 0:
            ######## LOGIN ########
            if self.authenticate():
                self.isLogged = True
                self.bot.send_message(self.data["chat_id"], messages["login_success"])
            else:
                self.bot.send_message(self.data["chat_id"], messages["login_failed"])
        else:
            ######## SIGNUP ########
            database = db()
            data = database.get_data()
            for i in data:
                if i["hostname"] == self.data["hostname"]:
                    self.bot.send_message(self.user.data["chat_id"], messages["hostname_taken"])
                    self.get_password_signup()
            database.insert_user(self.data)
            self.isLogged = True
            self.bot.send_message(self.data["chat_id"], messages["signup_success"])
    def logout(self, msg):
        if self.isLogged:
            self.isLogged = False
            self.order = None
            self.bot.send_message(self.data["chat_id"], messages["logout"])
            self.data = {"hostname" : None, "password": None, "chat_id": msg.chat.id}
        else:
            self.bot.send_message(self.data["chat_id"], messages["not_logged_in_error"])
    def authenticate(self):
        database = db()
        data = database.get_data()
        for i in data:
            if (i["hostname"] == self.data["hostname"]) and (i["password"] == self.data["password"]):
                return True
        return False