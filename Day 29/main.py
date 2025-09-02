from tkinter import Tk, PhotoImage, Canvas, Label, Entry, Button, END, messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """generate a random secure password"""
    from random import randint, choice, shuffle
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        messagebox.showerror(title="Error", message="Please enter all fields")
    else:
        is_valid_input = messagebox.askokcancel(title="Password Validation", message=f"Are you sure to save this data:\nWebsite: {website_data}\nEmail: {email_data}\nPassword: {password_data}")
        if is_valid_input:
            with open("data.txt", "a") as data:
                line = f"{website_data} | {email_data} | {password_data}\n"
                data.write(line)
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            email_entry.insert(0, "janeDoe@gmail.com")
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window
my_window = Tk()
my_window.title("Password Manager")
my_window.config(padx=50, pady=50)

# Image
password_img = PhotoImage(file="logo.png")

# Canvas
my_canvas = Canvas(width=200, height=200, highlightthickness=0)
my_canvas.create_image(100, 100, image=password_img)
my_canvas.grid(row=0, column=1)

# Website
website_label = Label(text="Website")
website_label.grid(row=1, column=0)

# Website Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# Email
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)

# Email Entry
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "janeDoe@gmail.com")

# Password Label
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Password Entry
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Password Generator Button
password_generator_button = Button(text="Generate Password", command=generate_password)
password_generator_button.grid(row=3, column=2)

# Add Button
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=3)
add_button.config(command=save)

my_window.mainloop()