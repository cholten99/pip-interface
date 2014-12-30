#!/usr/bin/python
import sys
import requests
import json
from wtw import * 
def process_message(message):
  # Get the entry from mongoDB via an http request
  message = json.loads(message)
  # Brief pause set processing state via http
  handle_command(message, app_commands)
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
    print "Unexpected error:", sys.exc_info()[0]
#    continue
