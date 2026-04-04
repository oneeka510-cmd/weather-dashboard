import streamlit as st
import requests
import os
from dotenv import load_dotenv
import folium
from streamlit_folium import st_folium

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Base URL for OpenWeather API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetch weather data for a given city"""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def get_weather_icon(icon_code):
    """Get weather icon URL from OpenWeather"""
    return f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

# ---------- UI ----------
st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="🌤️",
    layout="centered"
)

st.title("🌤️ Weather Dashboard")
st.write("Enter a city name to get the current weather")

city = st.text_input("City Name", placeholder="e.g. Delhi, London, New York")

if city:
    data = get_weather(city)

    if data.get("cod") != 200:
        st.error("City not found! Please check the spelling.")
    else:
        # Extract data
        city_name   = data["name"]
        country     = data["sys"]["country"]
        temp        = data["main"]["temp"]
        feels_like  = data["main"]["feels_like"]
        humidity    = data["main"]["humidity"]
        wind_speed  = data["wind"]["speed"]
        description = data["weather"][0]["description"].capitalize()
        icon_code   = data["weather"][0]["icon"]
        lat         = data["coord"]["lat"]
        lon         = data["coord"]["lon"]

        # ---------- Weather Card ----------
        st.success(f"📍 {city_name}, {country}")

        # Icon + Description
        col_icon, col_desc = st.columns([1, 3])
        with col_icon:
            st.image(get_weather_icon(icon_code), width=80)
        with col_desc:
            st.markdown(f"### {description}")
            st.markdown(f"🌡️ **{temp}°C** — Feels like {feels_like}°C")

        st.divider()

        # 3 metric cards
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("🌡️ Temperature", f"{temp}°C")
        with col2:
            st.metric("💧 Humidity", f"{humidity}%")
        with col3:
            st.metric("💨 Wind Speed", f"{wind_speed} m/s")

        st.divider()

        # ---------- Map ----------
        st.subheader("🗺️ Location")
        m = folium.Map(location=[lat, lon], zoom_start=10)
        folium.Marker(
            location=[lat, lon],
            popup=f"{city_name}: {temp}°C, {description}",
            tooltip=city_name,
            icon=folium.Icon(color="blue", icon="cloud")
        ).add_to(m)

        st_folium(m, width=700, height=400)