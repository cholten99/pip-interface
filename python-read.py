#!/usr/bin/python
import pika
import pymongo
from bson.objectid import ObjectId
import time
# Setup callback to access mongoDB
client = pymongo.MongoClient("localhost", 27017)
db = client.pipinterface
def callback(ch, method, properties, body):
  # Ackowledge RabbitMQ
  ch.basic_ack(delivery_tag = method.delivery_tag)
  # Get the entry from mongoDB
  uid_object = ObjectId(body)
  pip_entry = db.pipinterface.find( { "_id": uid_object } )[0]
  # Brief pause
  db.pipinterface.update({"_id": uid_object}, {"$set":{"ProcStatus": "Processing"}})
  print " [x] Received %r" % (pip_entry,) + " -- Sleeping " + str(random_pause) + " seconds"
  random_pause = pip_entry["WaitTime"]
  time.sleep(random_pause)
  # Set final processing status
  db.pipinterface.update({"_id": uid_object}, {"$set":{"ProcStatus": "Processed"}})
# Get uid from RabbitMQ queue
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue='pipinterface')
channel.basic_consume(callback, queue="pipinterface")
channel.start_consuming()
