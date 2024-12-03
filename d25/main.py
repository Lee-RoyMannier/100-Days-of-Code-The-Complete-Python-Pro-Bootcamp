import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json


def password_gen():
    password_entry.delete(0, tk.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)


def seach_web():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            web = data[web_entry.get()]
    except KeyError:
        messagebox.showerror(message="Pas de site trouvé")
    else:
        email_entry.delete(0, tk.END)
        email_entry.insert(0, web["email"])
        password_entry.insert(0, web["password"])


def save_data():
    website = web_entry.get()
    email = email_entry.get()
    pwd = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": pwd
        }
    }

    if len(website) == 0 or len(email) == 0 or len(pwd) == 0:
        messagebox.ERROR = 'error'

        messagebox.showerror(
            "Error", message="Une information n'est pas rentrée")
    else:
        input_data = messagebox.askokcancel(
            "Confirmation", message="Les informations sont save")
        if input_data:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                web_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)


screen = tk.Tk()
screen.title("Password Manager")
screen.config(padx=20, pady=20, bg="white")


canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

web_label = tk.Label(text="Website:", bg="white", fg="black")
web_label.grid(column=0, row=1)

username_label = tk.Label(text="Email/Username:",  bg="white", fg="black")
username_label.grid(column=0, row=2)

password_label = tk.Label(text="Password:",  bg="white", fg="black")
password_label.grid(column=0, row=3)

web_entry = tk.Entry(width=35,
                     highlightthickness=0)
web_search = tk.Button(text="Search", command=seach_web)
web_entry.focus()
web_entry.grid(column=1, row=1)
web_search.grid(column=2, row=1, columnspan=2)

email_entry = tk.Entry(width=35,  highlightthickness=0)
email_entry.insert(tk.END, "test@hotmail.fr")
email_entry.grid(column=1, row=2)

password_entry = tk.Entry(width=36,  highlightthickness=0)
generate_btn = tk.Button(text="Generate Password",
                         bg="white", highlightthickness=0, command=password_gen)
password_entry.grid(column=1, row=3)
generate_btn.grid(column=2, row=3, columnspan=2)
add_btn = tk.Button(text="Add", width=36, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)
screen.mainloop()
