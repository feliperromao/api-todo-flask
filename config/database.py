from pymongo import MongoClient

DB_URL = 'mongodb://todo_db:27017/'
DB_NAME = 'todo_api'

client = MongoClient(DB_URL)

db = client[DB_NAME]