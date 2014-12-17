#!/usr/bin/python
import pika
import pymongo
from bson.objectid import ObjectId
import time
import random
import requests
import json
from wtw import wtw_notepad
def callback(ch, method, properties, body):
  # Ackowledge RabbitMQ
  ch.basic_ack(delivery_tag = method.delivery_tag)
  # Get the entry from mongoDB via an http request
  get_url = "http://bowsy.co.uk/web-to-windows/php-mongo-get.php?uid=" + body
  resp_text = requests.get(get_url)
  resp_dict = json.loads(resp_text.text)
  # Brief pause set processing state via http
  random_pause = random.randint(1, 3)
  wtw_notepad(resp_dict["Name"], resp_dict["Age"])
  print(" [x] Sleeping " + str(random_pause) + " seconds")
  time.sleep(random_pause)
  # Set final processing status via http
  post_payload = {'uid': body}
  post_response = requests.post("http://bowsy.co.uk/web-to-windows/php-mongo-post.php", data = post_payload)

# MAIN : Get uids from RabbitMQ queue
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue='wtwinterface')
channel.basic_consume(callback, queue="wtwinterface")
channel.start_consuming()
