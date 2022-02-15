from tkinter import *


def button_click():
    conversion = int(input.get()) * 1.6
    conversion_label.config(text=str(conversion))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(200, 100)

input = Entry()
input.grid(column=0, row=1)

mile_label = Label(text="label", font=("Arial", 24))
mile_label.config(text="Miles")
mile_label.grid(column=2, row=0)

equal_label = Label(text="label", font=("Arial", 24))
equal_label.config(text="is equal to")
equal_label.grid(column=0, row=1)

conversion_label = Label(text="label", font=("Arial", 24))
conversion_label.config(text="0")
conversion_label.grid(column=1, row=1)

kilometer_label = Label(text="label", font=("Arial", 24))
kilometer_label.config(text="Km")
kilometer_label.grid(column=2, row=1)

input = Entry(width=10)
input.grid(column=1, row=0)

button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)


window.mainloop()
