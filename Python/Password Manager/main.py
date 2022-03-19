from random import choice, randint, shuffle
from tkinter import messagebox, Tk, Canvas, PhotoImage, Label, Entry, Button
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(numbers) for _ in range(randint(2, 4))]
    number_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)

    generated_password = "".join(password_list)

    pwd_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pwd_entry.get()
    if len(website) > 0 and len(email) > 0:
        pwd_details = f"{website} | {email} | {password}\n"
        user_consent = messagebox.askokcancel(title=website,
                                              message=f"Here are the details\n Email: {email}\n "
                                                      f"Password: {password}\n Do you want to save?")
        if user_consent:
            website_entry.delete(0, 'end')
            pwd_entry.delete(0, 'end')
            with open("data.txt", mode='a') as file:
                file.writelines(pwd_details)
            messagebox.showinfo(title="Password Manager", message="Credentials Saved Successfully")
    else:
        messagebox.showwarning(title="Error", message="Please enter all the details")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
image_file = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_file)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
pwd_label = Label(text="Password:")
pwd_label.grid(row=3, column=0)

website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "test@mailinator.com")
pwd_entry = Entry(width=21)
pwd_entry.grid(row=3, column=1, sticky="EW")

gen_pwd_btn = Button(text="Generate Password", command=generate_password)
gen_pwd_btn.grid(row=3, column=2, sticky="EW")
add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
