from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# load environment variables from .env file
load_dotenv()

def get_current_weather(city="Mangalore"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    
    # make the API request
    weather_data = requests.get(request_url).json()  
    return weather_data

if __name__ == "__main__":
    print('\n*** Get current Weather conditions ***\n')
    city = input("\nPlease enter city name: ")
    
    # default to Mangalore if the input is empty
    if not bool(city.strip()):
        city = "Mangalore"
        
    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)
