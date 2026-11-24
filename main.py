
from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady= 20, padx= 20)

canvas = Canvas(width= 200, height= 200)
logo_img = PhotoImage(file= 'logo.png')
canvas.create_image(100, 100, image= logo_img)
canvas.pack()


website_label = Label(text= 'Website')
website_label.pack()

email_label = Label(text= "Email/Usernmae")
email_label.pack()

password_label = Label(text='Password')
password_label.pack()



website_entry = Entry(width=35)
website_entry.pack()

email_entry = Entry(width= 35)
email_entry.pack()

password_entry = Entry (width= 35)
password_entry.pack()



generate_button = Button(text= 'Generate')
generate_button.pack()

add_button = Button( text= 'Add')
add_button.pack()

window.mainloop()