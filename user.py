from threading import Timer
import pymongo
from db import db

class User:
    def __init__(self):
        self.state = 0
        self.ASKING_USERNAME = 0
        self.ASKING_PASSWORD = 1
        self.READY_TO_AUTHHENTICATE = 2
        self.data = {"username": None, "password": None, "chat_id": None}
        self.isLogged = False
    def authenticate(self):
        database = db()
        data = database.get_data()
        for i in data:
            if (i["username"] == self.data["username"]) and (i["password"] == self.data["password"]):
                return True
        return False