import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import datetime
import os

# ---------------- COLORS ----------------
BG_COLOR = "#1e1e2f"
CARD_COLOR = "#2c2c3e"
BTN_COLOR = "#4CAF50"
TEXT_COLOR = "#ffffff"
ENTRY_BG = "#3a3a4f"

# ---------------- BMI LOGIC ----------------
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        return round(bmi, 2), "Underweight"
    elif bmi < 24.9:
        return round(bmi, 2), "Normal"
    elif bmi < 29.9:
        return round(bmi, 2), "Overweight"
    else:
        return round(bmi, 2), "Obese"

# ---------------- SAVE DATA ----------------
def save_data(name, bmi):
    with open("bmi_data.txt", "a") as f:
        f.write(f"{name},{bmi},{datetime.datetime.now()}\n")

# ---------------- LOAD DATA ----------------
def load_data(name):
    data = []
    if not os.path.exists("bmi_data.txt"):
        return data

    with open("bmi_data.txt", "r") as f:
        for line in f:
            user, bmi, date = line.strip().split(",")
            if user == name:
                data.append(float(bmi))
    return data

# ---------------- GRAPH ----------------
def show_graph():
    name = name_entry.get()
    data = load_data(name)

    if not data:
        messagebox.showinfo("Info", "No data available")
        return

    plt.figure("BMI Trend")
    plt.plot(data, marker='o')
    plt.title(f"BMI Trend for {name}")
    plt.xlabel("Records")
    plt.ylabel("BMI")
    plt.grid()
    plt.show()

# ---------------- CALCULATE ----------------
def calculate():
    try:
        name = name_entry.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError

        bmi, category = calculate_bmi(weight, height)

        result_label.config(
            text=f"BMI: {bmi} ({category})",
            fg="#00ffcc"
        )

        save_data(name, bmi)

    except:
        messagebox.showerror("Error", "Enter valid inputs!")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x450")
root.config(bg=BG_COLOR)

# Title
title = tk.Label(root, text="BMI Calculator",
                 font=("Arial", 20, "bold"),
                 bg=BG_COLOR, fg=TEXT_COLOR)
title.pack(pady=10)

# Card Frame
frame = tk.Frame(root, bg=CARD_COLOR, bd=5, relief="ridge")
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Name
tk.Label(frame, text="Name", bg=CARD_COLOR, fg=TEXT_COLOR).pack(pady=5)
name_entry = tk.Entry(frame, bg=ENTRY_BG, fg=TEXT_COLOR)
name_entry.pack(pady=5)

# Weight
tk.Label(frame, text="Weight (kg)", bg=CARD_COLOR, fg=TEXT_COLOR).pack(pady=5)
weight_entry = tk.Entry(frame, bg=ENTRY_BG, fg=TEXT_COLOR)
weight_entry.pack(pady=5)

# Height
tk.Label(frame, text="Height (m)", bg=CARD_COLOR, fg=TEXT_COLOR).pack(pady=5)
height_entry = tk.Entry(frame, bg=ENTRY_BG, fg=TEXT_COLOR)
height_entry.pack(pady=5)

# Buttons
calc_btn = tk.Button(frame, text="Calculate BMI",
                     bg=BTN_COLOR, fg="white",
                     font=("Arial", 12, "bold"),
                     command=calculate)
calc_btn.pack(pady=10)

graph_btn = tk.Button(frame, text="Show Graph",
                      bg="#2196F3", fg="white",
                      font=("Arial", 12, "bold"),
                      command=show_graph)
graph_btn.pack(pady=5)

# Result
result_label = tk.Label(root, text="",
                        font=("Arial", 14, "bold"),
                        bg=BG_COLOR, fg="#00ffcc")
result_label.pack(pady=10)

root.mainloop()