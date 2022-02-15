from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)
email_user = Label(text="Email/Username:")
email_user.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

web_input = Entry(width=52)
web_input.grid(column=1, row=1, columnspan=2, sticky='w')
web_input.focus()
email_user_input = Entry(width=52)
email_user_input.grid(column=1, row=2, columnspan=2, sticky='w')
email_user_input.insert(0, "gr@gmail.com")
password_input = Entry(width=33)
password_input.grid(column=1, row=3, columnspan=2, sticky='w')

password_button = Button(text="Generate Password")
password_button.grid(column=2, row=3, sticky='e')

add_button = Button(text="Add", width=44)
add_button.grid(column=1, row=4, columnspan=2, sticky='w')

window.mainloop()
