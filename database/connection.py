from config import config
from pymongo import MongoClient

db = MongoClient(config.MONGODB_URI)[config.DB_NAME]