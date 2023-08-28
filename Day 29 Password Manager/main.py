from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_number

    shuffle(password_list)

    password = ''.join(password_list)

    # print(f"Your password is: {password}")

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askyesno(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                           f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("saved-password.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create Canvas
canvas = Canvas(width=200, height=200)
password_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_logo)
canvas.grid(column=1, row=0)

# Website Label and Entry
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=54)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Email/Username Label and Entry
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=54)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "sudeepsudhevan@gmail.com")

# Password and Entry
password_label = Label(text="Password:", width=21)
password_label.grid(column=0, row=3)

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

# Generate Password Button
pass_gen_button = Button(text="Generate Password", command=password_generator)
pass_gen_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=46, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
