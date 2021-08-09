from threading import Timer
import pymongo
from db import db

class User:
    def __init__(self, bot):
        self.bot = bot
        self.state = 0
        self.ASKING_USERNAME = 0
        self.ASKING_PASSWORD = 1
        self.READY_TO_AUTHHENTICATE = 2
        self.data = {"hostname" : None, "password": None, "chat_id": None}
        self.isLogged = False
    def get_hostname(self, msg):
        self.data["hostname"] = msg.text
        self.bot.send_message(self.data["chat_id"], "Contraseña")
        self.bot.register_next_step_handler(msg, self.get_password)
    def get_password(self, msg, auth=False):
        self.data["password"] = msg.text
        if auth:
            if self.authenticate():
                self.isLogged = True
                self.bot.send_message(self.data["chat_id"], "Usuario autenticado con éxito")
            else:
                self.bot.send_message(self.data["chat_id"], "Error, inténtelo de nuevo")
        else:
            database = db()
            #data = database.get_data()
            database.insert_user(self.data)
            self.isLogged = True
            self.bot.send_message(self.data["chat_id"], "Usuario registrado con éxito")
    def authenticate(self):
        database = db()
        data = database.get_data()
        for i in data:
            if (i["hostname"] == self.data["hostname"]) and (i["password"] == self.data["password"]):
                return True
        return False