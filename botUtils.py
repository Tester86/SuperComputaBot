import telebot
import paramiko
from time import sleep
import requests
from user import User
import json
import pymongo

bot = telebot.TeleBot("1711714436:AAGIcTRmYJR8NhKxZJovXawhnuW9lWBRxdk")
client = pymongo.MongoClient("mongodb+srv://admin:__supercomputabot86@cluster0.mf5cv.mongodb.net/DIPC?retryWrites=true&w=majority")
coll = client.DIPC.users

"""def connect_to_cluster(num):
    vm = paramiko.SSHClient()
    vm.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    vm.connect("81.38.120.156", 22, "Germa", "04022004", timeout=20)
    stdin, stdout, stderr = vm.exec_command("ifconfig")
    result = stdout.read().decode("UTF-8")
    print(result)
    """

def is_user(chat_id):
    data = coll.find()
    for i in data:
        if int(i["chat_id"]) == int(chat_id):
            return (True, int(chat_id))
    return (False, None)
        

def initialize(msg, user):
    LOGIN_ORDER = 0
    SIGNUP_ORDER = 1
    user.data["chat_id"] = int(msg.chat.id)
    if(is_user(user.data["chat_id"])[0]):
        return (user, LOGIN_ORDER)
    else:
        return (user, SIGNUP_ORDER)

def authenticate(msg, username, password):
    data = coll.find()
    for i in data:
        if (username == i["username"]) and (password == i["password"]):
            return True
    return False