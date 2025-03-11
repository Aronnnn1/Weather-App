import tkinter as tk
from tkinter import messagebox, ttk
import requests
from datetime import datetime
from PIL import Image,ImageTk
class Weather():
    def get_weather(self,city):
        api_key = "3128ab875a8b4195e3553392b24a81bb"  
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
        }
        response = requests.get(base_url, params=params)
        return response.json()

    def show_weather(self):
        city = city_var.get()
        if city:
            weather_data = self.get_weather(city)
            if weather_data.get('cod') == 200:
                
                temperature = weather_data['main']['temp']
                description = weather_data['weather'][0]['description']
                humidity = weather_data['main']['humidity']
                wind_speed = weather_data['wind']['speed']
                date_time = datetime.now().strftime("%A, %d %B %Y, %H:%M:%S")
                weather_label.config(text=f"Date & Time: {date_time}\nTemperature: {temperature}°C\nDescription: {description}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s")
            else:
                messagebox.showerror("Error", f"City not found: {weather_data.get('message', 'Unknown error')}")
        else:
            messagebox.showerror("Input Error", "Please select a city")

    def state(self):
        state=state_var.get()
        if state:
            city_menu['values']=list(CITIES[state])
        else:
            messagebox.showerror("Input Error", "Please enter a state name")
    


CITIES = {
    "Andhra Pradesh":["Hyderabad","Tirupati","Vijayawada","Nellore","Guntur","Visakhapatnam"],
    "Gujarat":["Ahmedabad","Vadodara","Rajkot","Gandhinagar","Dwarka","Surat"],
    "Karnataka":["Bangalore","Mangalore","Mysore","Udupi","Shivamogga","Belagavi","Kolar","Dharwad"],
    "Kerala":["Kochi","Kannur","Thiruvananthapuram","Kollam","Kozhikode","Kottayam","Kasaragod","Palakkad","Munnar"],
    "Tamil Nadu":["Chennai","Madurai","Salem","Coimbatore","Vellore","Thanjavur","Tiruppur","Kanchipuram","Dindigul","Hosur"],
    "Goa":["Panaji","Madgaon","Mapusa","Canacona","Calangute","Pernem","Vasco Da Gama",],
    "Telangana":["Warangal","Hyderabad","Nizamabad","Karimnagar","Suryapet","Nalgonda"],
    "Madhya Pradesh":["Indore","Bhopal","Gwalior","Jabalpur","Ujjain","Rewa","Dewas","Khandwa","Maheshwar"],
    "Rajasthan":["Udaipur","Jaipur","Jodhpur","Ajmer","Alwar","Beawar"],
    "Uttar Pradesh":["Lucknow","Agra","Noida","Ayodhya","Varanasi","Firozabad","Jhansi","Gorakhpur","Ghaziabad","Kanpur"],
    "Punjab":["Bathinda","Amritsar","Chandigarh","Ludhiana","Patiala","Kapurthala","Pathankot","Adampur","Raikot"],
    "Haryana":["Gurugram","Karnal","Faridabad","Panipat","Rewari","Ambala","Sonipat","Bilaspur"],
    "Bihar":["Patna","Gaya","Buxar","Bhagalpur","Darbhanga","Hajipur","Dehri","Nawada","Rajgir"],
    "Jharkhand":["Ranchi","Jamshedpur","Dhanbad","Deoghar","Godda","Chaibasa","Chas"],
    "Chhattisgarh":["Raipur","Korba","Bilaspur","Raigarh","Balod","Arang","Patan"],
    "Manipur":["Thoubal","Imphal","Kakching","Andra","Bishnupur"],
    "Mizoram":["Aizawl","Lunglei","Thenzawl","Sairang","Serchhip"],
    "Arunachal Pradesh":["Khonsa","Tezu","Itanagar","Ziro","Tawang"],
    "Nagaland":["Kohima","Dimapur","Mokokchung","Wokha","Tuensang"],
    "Himachal Pradesh":["Mandi","Manali","Kullu","Bilaspur","Shimla","Nahan","Dalhousie","Sundar Nagar"],
    "Tripura":["Agartala","Belonia","Udaipur","Kailashahar","Dharmanagar"],
    "Sikkim":["Gangtok","Namchi","Mangan","Soreng","Rangpo","Chungthang"],
    "Odisha":["Cuttack","Bhubaneswar","Brahmapur","Puri","Sambalpur","Rourkela"],
    "Uttarakhand":["Dehradun","Nainital","Haridwar","Rishikesh","Kashipur"],
    "Maharashtra":["Mumbai","Nagpur","Pune","Nashik","Aurangabad","Thane","Amravati","Kalyan"],
    "West Bengal":["Kolkata","Siliguri","Asansol","Howrah","Durgapur","Darjeeling","Haldia","Malda"]}

    

root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("500x500")

bg_image = Image.open(r"img python.jpeg")
bg_image = bg_image.resize((500, 500))
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=bg_photo)
background_label.place(relwidth=1,relheight=1)

state_label = tk.Label(root, text="Select State:")
state_label.pack(pady=5)

state_var = tk.StringVar()
state_menu = ttk.Combobox(root, textvariable=state_var, state="readonly")
state_menu['values'] = list(CITIES.keys())
state_menu.pack(pady=5)

obj=Weather()

state_button = tk.Button(root, text="Continue", command=obj.state)
state_button.pack(pady=5)

city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=5)
city_var = tk.StringVar()
city_menu = ttk.Combobox(root, textvariable=city_var, state="readonly")
city_menu.pack(pady=5)

city_button = tk.Button(root, text="Get Weather", command=obj.show_weather)
city_button.pack(pady=5)

weather_label = tk.Label(root,text='', font=("Helvetica", 15))
weather_label.pack()


root.mainloop()
