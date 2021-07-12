import telebot
import paramiko

bot = telebot.TeleBot("1711714436:AAGIcTRmYJR8NhKxZJovXawhnuW9lWBRxdk", parse_mode=None)

cluster_msg = "Please choose a cluster:\n\n1. Atlas\n2. Hemera\n3. Ponto"

def connect_to_cluster(num):
    vm = paramiko.SSHClient()
    vm.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    vm.connect("81.38.120.156", 22, "Germa", "04022004", timeout=20)
    stdin, stdout, stderr = vm.exec_command("ifconfig")
    result = stdout.read().decode("UTF-8")
    print(result)

def exec_login(msg):
    pass