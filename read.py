#!/usr/bin/python
import sys
import time
import random
import requests
import json
from wtw import wtw_notepad
def process_message(message):
  # Get the entry from mongoDB via an http request
  message_dict = json.loads(message)
  # Brief pause set processing state via http
  random_pause = random.randint(1, 3)
#  wtw_notepad(resp_dict["Name"], resp_dict["Age"])
  print(" [x] Sleeping " + str(random_pause) + " seconds")
  time.sleep(random_pause)
  # Set final processing status via http
  uid = message_dict["_id"]["$id"]
  post_payload = {'uid': uid}
  post_response = requests.post("http://bowsy.co.uk/web-to-windows/set-processed.php", data = post_payload)

# MAIN : Get message from queue
while True:
  try:
    message = requests.get("http://bowsy.co.uk/web-to-windows/get-message.php");
    process_message(message.text)
  except:
    continue
