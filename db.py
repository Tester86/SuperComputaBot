import pymongo

class db:
    def __init__(self):
        client = pymongo.MongoClient("mongodb+srv://admin:__supercomputabot86@cluster0.mf5cv.mongodb.net/DIPC?retryWrites=true&w=majority")
        self.coll = client.DIPC.users
        self.data = self.coll.find()
    def get_coll(self):
        return self.coll
    def get_data(self):
        return self.data
    def insert_user(self, user_data):
        self.coll.insert_one(user_data)
    