from tkinter import *


def button_click():
    print("I got clicked")
    my_label.config(text=input.get())


window = Tk()
window.title("First GUI Window")
window.minsize(500, 300)

my_label = Label(text="Ich bin ein Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=100, pady=200)

button = Button(text="Click Me", command=button_click)
button.grid(column=1, row=1)

new_button = Button(text="I'm new here", command=button_click)
new_button.grid(column=2, row=0)

input = Entry()
input.grid(column=3, row=2)

#print(input.get())

window.mainloop()
