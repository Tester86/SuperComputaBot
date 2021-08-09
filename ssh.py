import paramiko
from user import User
from botUtils import bot

class SSHClient:
    def __init__(self, cluster_addr, local_addr, hostname):
        self.client = paramiko.SSHClient()
        self.jhost = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.jhost.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.user = User()
        self.dest = (cluster_addr, 22)
        self.local = (local_addr, 22)
        self.hostname = hostname
    def connect(self):
        try:
            username = self.user.data["username"]
            password = self.user.data["password"]
            self.client.connect(hostname=self.hostname, username=username, password=password)
            return self.client
        except Exception as e:
            bot.send_message(self.user.data["chat_id"], str(e))
            return False
    def connect_cluster(self):
        client_transport = self.client.get_transport()
        channel = client_transport.open_channel("direct-tcpip", dest, local)
        
        cluster = "CLUSTER"
        username = self.user.data["username"]
        password = self.user.data["password"]
        
        try:
            self.jhost.connect(cluster, username=username, password=password, sock=channel)
            return self.jhost
        except Exception as e:
            bot.send_message(self.user.data["chat_id"], str(e))
            return False
    def connect_cluster_sftp(self):
        try:
            jhost = self.connect_cluster()
            transport = jhost.get_transport()
            sftp = paramiko.SFTPClient.from_transport(transport)
            return sftp
        except Exception as e:
            bot.send_message(self.user.data["chat_id"], str(e))
            return False