from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.utils import get_weather, generate_activities, get_random_city
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()


# Add this before your routes
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
async def read_index():
    with open("frontend/index.html") as f:
        return HTMLResponse(f.read())

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/recommendations")
async def get_recommendations():
    try:
        city = get_random_city()
        weather_data = get_weather(city['lat'], city['lon'], settings.openweather_api_key)
        activities = generate_activities(weather_data, city['name'], settings.gemini_api_key)
        return {
            "city": city['name'],
            "weather": weather_data,
            "activities": activities
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))