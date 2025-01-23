import google.generativeai as genai
import requests

moroccan_cities = [
    {"name": "Casablanca", "lat": 33.5731, "lon": -7.5898},
    {"name": "Marrakech", "lat": 31.6295, "lon": -8.0087},
    {"name": "Rabat", "lat": 34.0209, "lon": -6.8416},
    {"name": "Fes", "lat": 34.0181, "lon": -5.0078},
    {"name": "Tangier", "lat": 35.7595, "lon": -5.8340},
    {"name": "Agadir", "lat": 30.4278, "lon": -9.5981},
    {"name": "Meknes", "lat": 33.8945, "lon": -5.5477},
    {"name": "Oujda", "lat": 34.6816, "lon": -1.9087},
    {"name": "Kenitra", "lat": 34.2541, "lon": -6.5800},
    {"name": "Tetouan", "lat": 35.5762, "lon": -5.3684}
]

def get_random_city():
    import random
    return random.choice(moroccan_cities)

def get_weather(lat: float, lon: float, api_key: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def generate_activities(weather_data: dict, city_name: str, api_key: str):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    
    prompt = f"""
    Suggest 5 varied activities in {city_name}, Morocco suitable for:
    - Weather: {weather_data['weather'][0]['description']}
    - Temperature: {weather_data['main']['temp']}°C
    Return only a JSON array of activity objects with 'name', 'type', and 'description' fields.
    Example format:
    [
        {{"name": "Visit Hassan II Mosque", "type": "cultural", "description": "Explore this iconic seaside mosque..."}},
        {{"name": "Jardin Majorelle", "type": "outdoor", "description": "Stroll through the vibrant blue gardens..."}}
    ]
    """
    
    response = model.generate_content(prompt)
    return parse_activities(response.text)

def parse_activities(text: str):
    # Implement parsing logic based on Gemini's response format
    # This is simplified - you'll need to adjust based on actual output
    import json
    return json.loads(text)
