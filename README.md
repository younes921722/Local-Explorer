# Local Explorer 🌍  
**Discover personalized activities based on your location and weather!**  

## Features ✨  
- 🌦️ **Real-time weather integration** with OpenWeatherMap  
- 🤖 **AI-powered recommendations** using Google Gemini  
- 📍 **Location-based suggestions** with Google Maps integration  
- 🎯 **Dynamic activity filtering** (cultural, outdoor, food, etc.)  
- 🛠️ **Fallback mode** for random Moroccan city suggestions  

## Tech Stack 🛠️  
**Backend**:  
- Python 3.9+  
- FastAPI  
- Pydantic  
- Google Generative AI  

**Frontend**:  
- Bootstrap 5  
- Vanilla JavaScript  
- Responsive design  

**APIs**:  
- OpenWeatherMap API  
- Google Maps API  
- Google Gemini API  

## Directory Structure 📂  
├── README.md
├── app
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── config.cpython-39.pyc
│   │   ├── main.cpython-39.pyc
│   │   └── utils.cpython-39.pyc
│   ├── config.py
│   ├── main.py
│   ├── schemas.py
│   └── utils.py
├── frontend
│   ├── index.html
│   ├── static
│   └── styles.css
└── requirements.txt

## Installation 💻  
1. Clone repo:  
```bash  
git clone https://github.com/younes921722/local-explorer.git  
cd local-explorer  
```
2. Create virtual environment:

```bash  
python -m venv venv  
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3.Install dependencies:

```bash  
pip install -r requirements.txt  
```
4.Create .env file:

OPENWEATHER_API_KEY=your_key  
GEMINI_API_KEY=your_key  
GOOGLE_MAPS_API_KEY=your_key  

5.Run server:
```bash  
uvicorn app.main:app --reload  
```
