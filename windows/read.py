#!/usr/bin/python
import sys
import time
import random
import requests
import json
from wtw import * 
def process_message(message):
  # Get the entry from mongoDB via an http request
  message = json.loads(message)
  # Brief pause set processing state via http
  random_pause = random.randint(1, 3)
  handle_command(message, app_commands)
  print(" [x] Sleeping " + str(random_pause) + " seconds")
  time.sleep(random_pause)
  # Set final processing status via http
  uid = message["_id"]["$id"]
  post_payload = {'uid': uid}
  post_response = requests.post("http://bowsy.co.uk/web-to-windows/web/set-processed.php", data = post_payload)

# MAIN : Get message from queue
app_commands = load_commands()
start_apps(app_commands)
while True:
  try:
    message = requests.get("http://bowsy.co.uk/web-to-windows/web/get-message.php");
    process_message(message.text)
  except KeyboardInterrupt:
    exit()
  except:
    continue
