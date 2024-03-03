'''
title: World's Worst GUI
authour: Michelle Liu
date: 4/03/24
version: 1
'''

#---IMPORTS
from guizero import App, Text

#---APP
app = App("it's all gone wrong", bg="dark green")
title = Text(app, text= "Some hard to read text", size="14", font="Comic Sans", color="green")

#---FUNCTIONS

def flash_text(): # makes unreadable text flash
    if title.visible:
        title.hide()
    else:
        title.show()

#---DISPLAY
app.repeat(1000, flash_text)
#repeat function makes flash_text function run every 1000 milliseconds(1 sec)

        
app.display()
