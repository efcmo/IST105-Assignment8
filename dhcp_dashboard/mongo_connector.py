from pymongo import MongoClient

db = None  # 👈 global variable

def init_mongo():
    global db
    MONGO_HOST = "172.31.3.220"
    MONGO_PORT = 27017
    MONGO_DB = "networkDB"

    try:
        client = MongoClient(MONGO_HOST, MONGO_PORT, serverSelectionTimeoutMS=2000)
        client.admin.command('ping')
        db = client[MONGO_DB]
        print(f"✅ MongoDB connected at {MONGO_HOST}")
    except Exception as e:
        print(f"❌ Failed to connect MongoDB: {e}")
        db = None

