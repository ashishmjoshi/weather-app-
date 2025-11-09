import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    api_key = "your_api_key_here"  # Replace with your actual API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data['main']['temp']
            desc = data['weather'][0]['description']
            result_label.config(text=f"🌡️ {temp}°C\n🌥️ {desc.capitalize()}")
        else:
            result_label.config(text="❌ City not found")
    except Exception as e:
        result_label.config(text="⚠️ Error fetching data")

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")

tk.Label(root, text="Enter City Name:").pack(pady=5)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()