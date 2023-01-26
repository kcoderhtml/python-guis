from guizero import *
import hashlib

def check_pass():
    if hashlib.sha224(bytes(verify.value, encoding='utf-8')).hexdigest() == '0f2ce955da2632f93114a00767ac8c69090ff6e1f98e09634ab5408a':
        app.info("Password Recegnized", "Password Recegnized!")
    else:
        app.error("Password Not Recegnized", "Password Not Recegnized!")

app = App(title="Password", width=400, height=300, layout="auto")

verify = TextBox(app)

update_text = PushButton(app, command=check_pass, text="Check Password")
