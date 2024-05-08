from tkinter import *
from tkinter import messagebox
import pyperclip

import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    
    password_list =  password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    
    password = "".join(password_list)
    
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
        website = website_entry.get()
        name = name_entry.get()
        password = password_entry.get()
        
        if (len(website) == 0 or len(password) == 0):
            messagebox.showinfo(title = "Error", message="Make sure that there are no blank fields")
            
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {name} "
                                    f"\nPassword: {password} \n Is it ok to save?")
        
        if is_ok:
            with open(file='./data.txt', mode='a') as data:
                data.write(f'{website} || {name} || {password} \n')
                website_entry.delete(0,END)
                name_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title(string="Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels

website_text = Label(text="Website:")
website_text.grid(row=1, column=0)

name_text = Label(text="Username/email:")
name_text.grid(row=2, column=0)

password_text = Label(text="Password:")
password_text.grid(row=3, column=0)
#Buttons

gen_pass_button = Button(text="Generate Password", command=generate)
gen_pass_button.grid(row=3, column=3)

add_button = Button(text="Add Password", command=add, width=36)
add_button.grid(row=4, column=1, columnspan=2)

#Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()

name_entry = Entry(width=35)
name_entry.grid(row=2, column=1)
name_entry.insert(index=0,string="defaultname")

password_entry = Entry(text="Password", width=35)
password_entry.grid(row=3, column=1)

window.mainloop()