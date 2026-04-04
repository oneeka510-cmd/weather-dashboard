<img width="1003" height="906" alt="image" src="https://github.com/user-attachments/assets/e6bbbc8d-5a75-425a-afa1-795677aa5a0a" />
# 🌤️ Weather Dashboard

A real-time weather dashboard built with Python and Streamlit. Enter any city name to get current weather data along with an interactive map.

---

## 📸 Demo

> Add your demo video or screenshot here

---

## ✨ Features

- 🌡️ Real-time temperature, feels like, humidity and wind speed
- 🗺️ Interactive map with city marker using Folium
- 🌤️ Live weather icon from OpenWeather
- 🐳 Fully Dockerized for consistent environments
- 🔐 Secure API key handling via environment variables

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | UI framework |
| OpenWeather API | Weather data |
| Folium | Interactive map |
| Docker | Containerization |
| Railway | Deployment |

---

## 🚀 Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/oneeka510-cmd/weather-dashboard.git
cd weather-dashboard
```

### 2. Set up environment variables

Create a `.env` file in the root folder:

```
OPENWEATHER_API_KEY=your_api_key_here
```

Get a free API key at 👉 [https://openweathermap.org/api](https://openweathermap.org/api)

### 3. Run with Docker (recommended)

```bash
docker build -t weather-dashboard .
docker run -p 8501:8501 --env-file .env weather-dashboard
```

Open 👉 [http://localhost:8501](http://localhost:8501)

### 4. Run without Docker

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

pip install -r requirements.txt
streamlit run app.py
```

---

## 📁 Project Structure

```
weather-dashboard/
├── app.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker config
├── docker-compose.yml   # Docker Compose config
├── .env                 # API key (not committed)
├── .env.example         # Safe placeholder for others
└── .gitignore
```

---

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `OPENWEATHER_API_KEY` | Your OpenWeather API key |

---

## 📚 What I Learned

This was intentionally a simple project — the goal was to learn and practice:

- Containerizing a Python app with **Docker**
- Managing **virtual environments** and dependencies
- Handling **API keys** securely in production
- **Deploying** a live app on Railway

---

## 📄 License

MIT License — feel free to use and modify!
