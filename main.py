import tkinter as tk
from tkinter import Entry, messagebox
import secrets
import string
import hashlib
import csv
import pyperclip

def generate_password():
    # Define character sets for password generation
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each set is included
    password = (
        secrets.choice(lowercase_letters) +
        secrets.choice(uppercase_letters) +
        secrets.choice(digits) +
        secrets.choice(symbols) +
        ''.join(secrets.choice(lowercase_letters + uppercase_letters + digits + symbols) for _ in range(8))
    )

    # Shuffle the password to ensure randomness
    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)

    # Update the password entry field
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)

def save_password():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if not website or not username or not password:
        messagebox.showwarning("Password Manager", "Please fill in all fields.")
        return

    # Hash the password before saving
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Save the password details to the CSV file
    with open('password.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([website, username, hashed_password])

    # Copy the password to the clipboard
    pyperclip.copy(password)

    messagebox.showinfo("Password Manager", "Password Saved Successfully!")

# Create the main window
root = tk.Tk()
root.title("Password Manager")

# Load and display the logo image
logo_image = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(root, image=logo_image)
logo_label.grid(row=0, column=0, columnspan=3, pady=(10, 0))

# Labels
label_website = tk.Label(root, text="Website:")
label_website.grid(row=1, column=0, pady=5, padx=10, sticky="w")

label_username = tk.Label(root, text="Username:")
label_username.grid(row=2, column=0, pady=5, padx=10, sticky="w")

label_password = tk.Label(root, text="Password:")
label_password.grid(row=3, column=0, pady=5, padx=10, sticky="w")

# Entry widgets
entry_website = Entry(root, width=30)
entry_website.grid(row=1, column=1, pady=5, padx=10)

entry_username = Entry(root, width=30)
entry_username.grid(row=2, column=1, pady=5, padx=10)

entry_password = Entry(root, width=30, show="*")
entry_password.grid(row=3, column=1, pady=5, padx=10)

# Button for generating passwords
button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.grid(row=3, column=2, pady=5, padx=10)

# Button for saving passwords
button_save = tk.Button(root, text="Save Password", command=save_password)
button_save.grid(row=4, column=1, pady=5, padx=10, columnspan=2, sticky="nsew")

# Run the Tkinter main loop
root.mainloop()
