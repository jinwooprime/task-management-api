from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")

uri = f""

client = MongoClient(uri, server_api=ServerApi("1"))

db = client.
collection = db[""]

