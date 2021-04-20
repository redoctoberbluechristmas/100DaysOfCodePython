from tkinter import *
from tkinter import messagebox  #< --- not a class, just a module, which is why * didn't bring it.
from random import choice, randint
import pyperclip  # <----useful way to get things into clipboard
import json
from os import path

WHITE = "#ffffff"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(23, 24))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    random.shuffle(password_list)

    # Join together all elements of list, password_list, to make one password.
    password = "".join(password_list)

    print(f"Your password is: {password}")
    pyperclip.copy(password)
    password_entry.insert(END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty fields", message="Hi, please don't leave any fields empty")
    else:
        password_list = {}
        try:
            with open("password.json", mode="r") as passwords:
                try:
                    password_list = json.load(passwords)  # <---- json.load reads password.json, populates existing.
                except json.decoder.JSONDecodeError: #<--- if no entries in password.json, skip.
                    pass
        except FileNotFoundError:  #<--- If there is no passwords.json, skip to finally where we create/edit it.
                pass

        finally:
            with open("password.json", mode="w") as passwords:
                password_list.update(new_data)
                json.dump(password_list, passwords, indent=4)  # <- converts from dict to json, writes to password.json
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- SEARCH FOR PASSWORD -------------------- #


def search_password():
    searched_website = website_entry.get()

    try:
        with open("password.json", mode="r") as passwords:
            answer = json.load(passwords)
    except FileNotFoundError:
        messagebox.showinfo(title="No Data", message="No Data File Found.")

    else:
        try:
            website_username = answer[searched_website]['email'] #< how to iterate through dict
            website_password = answer[searched_website]['password']
            messagebox.showinfo(title="Password", message=f"The username for {searched_website} is: {website_username}"
                                                          f"\nThe password for {searched_website} is {website_password}"
                                                          f".")
            pyperclip.copy(website_password)
        except KeyError:
            messagebox.showinfo(title="Password", message=f"No details for the website exist.")
            website_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus() # focus cursor on entry when the app runs.

email_entry = Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "kyjohns@protonmail.com")

password_entry = Entry(width=36)
password_entry.grid(row=3, column=1, columnspan=2)

# Buttons
search_button = Button(text="Search", width=20, command=search_password)
search_button.grid(row=1, column=2, columnspan=2)

generate_password_button = Button(text="Generate Password", width=20, command=generate_password)
generate_password_button.grid(row=2, column=2, columnspan=2)

save_password_button = Button(text="Add", width=20, command=save_password)
save_password_button.grid(row=3, column=2, columnspan=2)


window.mainloop()