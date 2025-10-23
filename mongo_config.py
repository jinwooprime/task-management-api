from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")

uri = f"mongodb+srv://{db_username}:{db_password}@backenddb.2ansun2.mongodb.net/?retryWrites=true&w=majority&appName=BackendDB"

client = MongoClient(uri, server_api=ServerApi("1"))

db = client.todo_db
collection = db["todo_data"]

