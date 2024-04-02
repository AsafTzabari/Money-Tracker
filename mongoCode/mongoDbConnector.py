from pymongo import MongoClient


def connect():
    # Connect with the portnumber and host
    myclient = MongoClient("mongodb://root:root@dbmongo:27017/?authMechanism=DEFAULT")
    # myclient = MongoClient("mongodb://root:root@localhost:8003/?authMechanism=DEFAULT")
    database = myclient["finance"]
    collection = database["transactions"]
    return collection


connect()
