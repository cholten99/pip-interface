from automa.api import *
import json 
import pprint
import ast
from os import listdir
from os.path import isfile, join

# Load the commands YAML
def load_commands():
  path = "../scripts/"
  app_commands = {}
  app_command_files = [ f for f in listdir(path) if isfile(join(path, f)) ]
  for app_command_file in app_command_files:
    app_name = app_command_file[:app_command_file.index('.')]
    file_handle = open(join(path, app_command_file))
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
                     "Wait_Window" : wait_window_comand
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
  wait_until(window(step["Wait_Window"]).exists)