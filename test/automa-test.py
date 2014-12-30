from automa.api import *
start("word")
write("Hello world!")
click("File")
click("Save")
click("Save")
wait_until(Window("Confirm Save As").exists)
click("Yes")