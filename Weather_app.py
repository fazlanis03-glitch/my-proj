#weather app using API
#user enters location and gets current weather data
import requests

API_KEY ="a00d257dce44187c0a3954d76196b2f3" #API tocken 

BASE_URL = "http://api.openweathermap.org/data/2.5/weather" #Base URL for the API

while True:

    city = input("Enter city name: ") 




    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric" 
   


    response = requests.get(url)


#covert to dictionary
    data = response.json()



    if response.status_code == 200: 
   
        print("Weather data for", city)
        print("Temperature:", data["main"]["temp"], "°C")
        print("Description:", data["weather"][0]["description"])
        print("Feels like:", data["main"]["feels_like"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Wind Speed:", data["wind"]["speed"], "m/s")
    else: 
        print("Error fetching data for", city)
    
    continue_search = input("\nSearch another city? (yes/no): ")
    if continue_search.lower() != "yes":
        break
