import pymongo

def connect_db():
    client = pymongo.MongoClient("mongodb+srv://admin:__04022004GCgc!@cluster0.8strf.mongodb.net/SuperComputaBot?retryWrites=true&w=majority")
    db = client["SuperComputaBot"]["users"]
    db.insert_one({"name": "Megan"})

connect_db()