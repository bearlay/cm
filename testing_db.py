import pymongo
import certifi
ca = certifi.where()

connection = pymongo.MongoClient("mongodb+srv://mrrobot:t00r@cluster0.4fo4qnv.mongodb.net/", tlsCAFile=ca)
database = connection["my_db1"]
collection=database["my_col1"]
data={'Mr.Robot':'CTF_Player','age':24,'Hobby':'BuildingTools'}
collection.insert_one(data)