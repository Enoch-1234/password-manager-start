from tkinter import *

from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_passwords():
   website = website_entry.get()
   email = email_entry.get()
   password = password_entry.get()

   messagebox.askyesno(title= website, message= f'user name: {email} \n password: {password}')
   with open('pass.txt', 'a') as data_file:
        data_file.write(f' {website}  | {email}  | {password} \n ')
        website_entry.delete(0, END)
        password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady= 50, padx= 50)

canvas = Canvas(width= 200, height= 200)
logo_img = PhotoImage(file= 'logo.png')
canvas.create_image(100, 100, image= logo_img)
canvas.grid(column=1, row=0)



website_label = Label(text= 'Website')
website_label.grid(column=0, row=1)

email_label = Label(text= "Email/Username")
email_label.grid(column= 0, row= 2)

password_label = Label(text='Password')
password_label.grid(column=0 , row= 3)



website_entry = Entry(width=35)
website_entry.grid(column=1,row=1, columnspan= 2)


email_entry = Entry(width= 35)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry (width= 26)
password_entry.grid(column=1, row=3)



generate_button = Button(text= 'Generate')
generate_button.grid(column=2, row=3, columnspan= 2)


add_button = Button( text= 'Add', width=35, command= add_passwords)
add_button.grid(column=1, row= 4, columnspan=2)

window.mainloop()