from pymongo import MongoClient

DB_URL = 'mongodb://localhost:27017/'
DB_NAME = 'todo_api'

client = MongoClient(DB_URL)

db = client[DB_NAME]