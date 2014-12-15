#!/usr/bin/python
import pymongo
import pika
import random
# Set up mongoDB
client = pymongo.MongoClient("localhost", 27017)
db = client.pipinterface
# Set up RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue='pipinterface')
# Loop input till enter "end" for name
name = raw_input("What is your name? ")
while (name != "end"):
  age = raw_input("What is your age? ")
  wait_time = random.randint(1, 10)
  # Save in mongoDB
  uid_object = db.pipinterface.save({"Name": name, "Age": age, "ProcStatus": "Pending", "WaitTime": wait_time})
  uid = str(uid_object)
  # Add to RabbitMQ queue
  channel.basic_publish(exchange='', routing_key="pipinterface", body=uid)
  name = raw_input("What is your name? ")
connection.close()
