from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

url = "mongodb-url"

# Create a new client and connect to the server
client = MongoClient(url, server_api=ServerApi('1'))

