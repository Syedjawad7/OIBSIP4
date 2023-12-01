import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            weather_info = f"Weather in {city}:\nTemperature: {data['main']['temp']}°C\nCondition: {data['weather'][0]['description']}"
            return weather_info
        else:
            return f"Error: {data['message']}"
    except Exception as e:
        return "Error:"


def get_weather_info():
    file_path = "C:\\Users\\DELL\\Desktop\\apikey.txt"
    try:
        with open(file_path, "r") as file:
            api_key = (
                file.read().strip()
            )  # Read the API key from the file as in my case it's apikey.txt
    except FileNotFoundError:
        print("The file does not exist")
        return

    city = entry.get()
    if not city:
        messagebox.showinfo("Error", "Please enter a city")
        return
    weather_info = get_weather(api_key, city)
    messagebox.showinfo("Weather Information", weather_info)


# GUI setup
app = tk.Tk()
app.title("Weather App")

label = tk.Label(app, text="Enter City:")
label.pack(pady=10)

entry = tk.Entry(app)
entry.pack(pady=10)

get_weather_button = tk.Button(app, text="Get Weather", command=get_weather_info)
get_weather_button.pack(pady=20)

img_icon = ImageTk.PhotoImage(file="C:\\Users\\DELL\Downloads\\weather-app.png")
app.iconphoto(False, img_icon)
app.configure(bg="#c8b6ff")  # (bg="#358600") "#6BAA75"
app.geometry("400x200")
app.mainloop()
