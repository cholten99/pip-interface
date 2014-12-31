# Setup
import os
import sys
import json
import ast
import pprint
sys.path.append(os.getcwd() + os.path.sep + 'automa\library.zip')
from automa.api import *

# Load the commands json
def load_commands():
  path = "../scripts/"
  app_commands = {}
  app_command_files = [ f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) ]
  for app_command_file in app_command_files:
    app_name = app_command_file[:app_command_file.index('.')]
    file_handle = open(os.path.join(path, app_command_file))
    app_commands[app_command_file[:app_command_file.index('.')]] = json.load(file_handle)
  return(app_commands)

# Start up the apps
def start_apps(app_commands):
  for app_name in app_commands:
    print "Starting " + app_name
    start(app_name)
 
def handle_command(message, app_commands):
  steps = app_commands[message["App"]][message["Command"]]["Steps"]
  for step in steps:
    handle_step(message, step)

def handle_step(message, step):
  automa_commands = {"Click" : click_command,
                     "Type" : type_command,
                     "Wait_Window" : wait_window_command
                    }
  command = step.keys()[0]
  switch_to(message['App'])
  automa_commands[command](message, step)

def click_command(message, step):
  clickable = ""
  if "$" in step["Click"] : 
    var_name = step["Click"][1:]
    clickable = message[var_name] 
  else:
    clickable = step["Click"]
    click(clickable)
 
def type_command(message, step):
  type_text = ""
  if "$" in step["Type"] :
    var_name = step["Type"][1:]
    type_text = message[var_name]
  else:
    type_text = step["Type"]
  write(type_text)

def wait_window_command(message, step):
  waiting_for = step["Wait_Window"]
  wait_until(Window(waiting_for).exists)	