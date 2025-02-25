from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


#SEARCH PASSWORD:
def search_password():
    website=web_input.get()
    try:
        with open("password-generator/data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found")
    else:
        if website in data:
            email=data[web_input.get()]["Email"]
            password=data[web_input.get()]["Password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Web not found", message=f"No passwords saved for {website}")

#PASSWORD GENERATOR:

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list=[choice(letters) for l in range(randint(8, 10))]
    password_list += [choice(symbols) for s in range(randint(2, 4))]
    password_list +=[choice(numbers) for n in range(randint(2, 4))]
    shuffle(password_list)

    password="".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
    
#SAVE PASSWORD:
def clear_all():
    web_input.delete(0,'end')
    email_input.delete(0,'end')
    email_input.insert(0, "@gmail.com")
    password_input.delete(0,'end')

def save():
    web=web_input.get()
    email=email_input.get()
    password= password_input.get()
    json_data= {web:{
        "Email": email,
        "Password": password}
    }

    if len(web)==0 or len(email)==0 or len(password)==0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty.")
    else:
        is_ok= messagebox.askokcancel(title=web, message=f"You entered the following details: \n Email:{email} \nPassword: {password} \n Is it ok to save?")

        if is_ok:
            try:
                with open("password-generator/data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("password-generator/data.json", "w") as data_file:
                    json.dump(json_data, data_file, indent=4)
            else:
                data.update(json_data)
                with open("password-generator/data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                clear_all()

#UI:
window = Tk()
window.title("Password Manager")
window.config(padx=45, pady=45)


canvas= Canvas(width=200, height=200)
logo=PhotoImage(file="password-generator/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

web_label= Label(text="Website:")
web_label.grid(row=1, column=0)

web_input=Entry(width=21)
web_input.grid(row=1, column=1)
web_input.focus()

search_button= Button(text="Search", width=15, command=search_password)
search_button.grid(row=1, column=2)

email_label=Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_input= Entry(width=40)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "@gmail.com")

password_label= Label(text="Password:")
password_label.grid(row=3, column=0)

password_input=Entry(width=21)
password_input.grid(row=3, column=1)

generate_pass=Button(text="Generate Password", width=15, command=generate_password)
generate_pass.grid(row=3, column=2)

add_button=Button(text="Add Password", width=38, command=save)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()
