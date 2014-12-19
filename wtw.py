from automa.api import *
import yaml

# Start by loading in the commands YAML
f = open("commands.yaml")
commands_dict = yaml.safe_load(f)
f.close()

def wtw_notepad(message_dict):
  print(" [x] Name: %s, age: %s" % (name, age))
