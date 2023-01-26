from guizero import *

def say_my_name():
    welcome_message.value = my_name.value

def change_text_size(slider_value):
    welcome_message.size = slider_value

app = App(title="Hello world")

welcome_message = Text(app, text="Welcome to my app")
welcome_message = Text(app, text="Welcome to my app", size=40, font="Times New Roman", color="darkblue")

my_name = TextBox(app)

update_text = PushButton(app, command=say_my_name, text="Display my name")

text_size = Slider(app, command=change_text_size, start=10, end=80)

my_cat = Picture(app, image="source.gif")

app.display()
