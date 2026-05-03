import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "86b0bb3256b6af77f86e211620d9fc8b"

def get_weather():
    city = city_entry.get().strip()

    if city == "":
        messagebox.showerror("Error", "Enter city name")
        return

    url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        print(data)  # DEBUG

        if data.get("cod") != 200:
            messagebox.showerror("Error", data.get("message", "API Error"))
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        result_label.config(
            text=f"City: {city}\nTemp: {temp}°C\nHumidity: {humidity}%\nCondition: {weather}"
        )

    except Exception as e:
        messagebox.showerror("Error", "Network or API issue")

# ---------------- UI ----------------
root = tk.Tk()
root.title("Weather App")
root.geometry("350x350")

tk.Label(root, text="Enter City").pack()

city_entry = tk.Entry(root)
city_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

root.mainloop()