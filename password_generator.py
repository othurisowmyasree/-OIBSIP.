import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# ---------------- PASSWORD LOGIC ----------------
def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            raise ValueError

        chars = ""

        if var_letters.get():
            chars += string.ascii_letters
        if var_numbers.get():
            chars += string.digits
        if var_symbols.get():
            chars += string.punctuation

        if chars == "":
            messagebox.showerror("Error", "Select at least one option")
            return

        password = "".join(random.choice(chars) for _ in range(length))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except:
        messagebox.showerror("Error", "Enter valid length")

# ---------------- COPY ----------------
def copy_password():
    pwd = password_entry.get()
    if pwd:
        pyperclip.copy(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard")
    else:
        messagebox.showerror("Error", "No password to copy")

# ---------------- UI ----------------
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.config(bg="#1e1e2f")

# Title
tk.Label(root, text="Password Generator",
         font=("Arial", 18, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=10)

# Length
tk.Label(root, text="Password Length",
         bg="#1e1e2f", fg="white").pack()
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Options
var_letters = tk.IntVar()
var_numbers = tk.IntVar()
var_symbols = tk.IntVar()

tk.Checkbutton(root, text="Include Letters",
               variable=var_letters,
               bg="#1e1e2f", fg="white",
               selectcolor="#2c2c3e").pack()

tk.Checkbutton(root, text="Include Numbers",
               variable=var_numbers,
               bg="#1e1e2f", fg="white",
               selectcolor="#2c2c3e").pack()

tk.Checkbutton(root, text="Include Symbols",
               variable=var_symbols,
               bg="#1e1e2f", fg="white",
               selectcolor="#2c2c3e").pack()

# Generate button
tk.Button(root, text="Generate Password",
          bg="#4CAF50", fg="white",
          command=generate_password).pack(pady=10)

# Output
password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)

# Copy button
tk.Button(root, text="Copy Password",
          bg="#2196F3", fg="white",
          command=copy_password).pack(pady=5)

root.mainloop()