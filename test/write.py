#!/usr/bin/python
import pymongo
import pika
import random
# Read in the names file
with open("names.txt") as file_handle:
  names_list = [line.rstrip() for line in file_handle]
# Set up mongoDB
client = pymongo.MongoClient("localhost", 27017)
db = client.wtwinterface
# Set up RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue='wtwinterface')
# Put lots of entries in the RabbitMQ queue 
for loop in range(0, 5):
  name = names_list[loop]
  age = random.randint(1, 99) 
  # Save in mongoDB
  uid_object = db.wtwinterface.save({"Name": name, "Age": age, "ProcStatus": "Pending"})
  uid = str(uid_object)
  # Add to RabbitMQ queue
  channel.basic_publish(exchange='', routing_key="wtwinterface", body=uid)
connection.close()
