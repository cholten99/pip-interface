#!/usr/bin/python
import pymongo
import pika
# Set up mongoDB
client = pymongo.MongoClient("localhost", 27017)
db = client.wtwinterface
# Set up RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue='wtwinterface')
# Add commands to mongoDB and the generated UIDs to RabbitMQ 
# ONE
uid_object = db.wtwinterface.save({"App": "Notepad", "Command": "Add", "Text": "Some text", "ProcStatus": "Pending"})
uid = str(uid_object)
channel.basic_publish(exchange='', routing_key="wtwinterface", body=uid)
# TWO
uid_object = db.wtwinterface.save({"App": "Notepad", "Command": "Add", "Text": "Some other text", "ProcStatus": "Pending"})
uid = str(uid_object)
channel.basic_publish(exchange='', routing_key="wtwinterface", body=uid)
# THREE
uid_object = db.wtwinterface.save({"App": "Notepad", "Command": "Delete",  "ProcStatus": "Pending"})
uid = str(uid_object)
channel.basic_publish(exchange='', routing_key="wtwinterface", body=uid)
# FOUR
uid_object = db.wtwinterface.save({"App": "Word", "Command": "Fish", "ProcStatus": "Pending"})
uid = str(uid_object)
channel.basic_publish(exchange='', routing_key="wtwinterface", body=uid)
# FIVE
uid_object = db.wtwinterface.save({"App": "Word", "Command": "Bobbins", "ProcStatus": "Pending"})
uid = str(uid_object)
channel.basic_publish(exchange='', routing_key="wtwinterface", body=uid)

client.close()
connection.close()
