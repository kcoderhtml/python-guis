from guizero import *

def mainfunc():
    def do_booking():
        verify = app.yesno("Verify Booking", "Are you sure you would like to book this seat?")
        if verify == True:
            app.info("Booking Successful", "Booking Successful.\n\nBye!")
            app.hide()
            exit()
            
        else:
            app.info("Booking Canceled", "Booking Canceled.")

    app = App(title="My second GUI app", width=400, height=300, layout="grid")

    film_choice = Combo(app, options=["Star Wars", "Frozen", "Frozen II", "Lion King", "Return of the Jedi"], grid=[1,0], align="left")
    film_description = Text(app, text="Which film?", grid=[0,0], align="left")

    vip_seat = CheckBox(app, text="VIP seat?", grid=[1,1], align="left")
    vip_description = Text(app, text="Seat Type", grid=[0,1], align="left")

    row_choice = ButtonGroup(app, options=[ ["Front", "Front"], ["Middle", "Middle"],["Back", "Back"] ],
    selected="Middle", horizontal=True, grid=[1,2], align="left")
    button_description = Text(app, text="Seat Location", grid=[0,2], align="left")

    book_seats = PushButton(app, command=do_booking, text="Book seat", grid=[1,3], align="left")

    app.display()

mainfunc()
