import random
import re
from random import choice
import requests
from guizero import *

def add(message):
    url = "https://www.gutenberg.org/files/1342/1342-0.txt"
    r = requests.get(url)
    text = r.text
    messages.append(text.split())

def hello():
    x = random.randint(0, len(messages) - 1)
    print(messages[x], end=" ")
    print(messages[x+1], end=" ")
    print(messages[x+2])

def get_file():
    file_name.value = app.select_file(folder="/home/kieran", filetypes=[["Text documents", "*.txt"]])

app = App()

PushButton(app, command=get_file, text="Get file")
file_name = Text(app)

app.display()
