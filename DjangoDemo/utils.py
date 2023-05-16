from pymongo import MongoClient


def get_db_handle(db_name):
    client = MongoClient("mongodb://localhost:27017")

    return client[db_name]