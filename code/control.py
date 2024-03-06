
from .code.models import User

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi



uri = "mongodb+srv://ig0rmota6678:TRuKlMtIKBdum3r5@cluster0.fxj1uaf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client['database']
users = db['Users']
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

def insertUser(user):
    user_data = {
        "name": user.name,
        "password": user.password,
        "email": user.email,
        "gender": user.gender,
        "tel": user.tel,
        "area": user.area,
        "occupation": user.occupation,
        "photo": user.photo,
    }
    users.insert_one(user_data)

    pass
def updateUser(user):
    pass
def deleteUser(user):
    pass

def checkUser(email, password):
    user = users.find_one({"email":email})
    if user:
        if password == user['password']:
            print("welcome back!")
        else:
            print("incorrect password!")
    else:
        print("kill yourself")
    pass