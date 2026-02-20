from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# 🔑 Put your OpenWeather API key here or as an environment variable
API_KEY = "bdf60badf23d07b761c42e48f111c2b2"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    return {
        "city": city,
        "temp": data["main"]["temp"],
        "description": data["weather"][0]["description"].title(),
        "humidity": data["main"]["humidity"]
    }


@app.route("/", methods=["GET"])
def index():
    city = request.args.get("city")
    weather = None

    if city:
        weather = get_weather(city)

    return render_template("index.html", weather=weather)


if __name__ == "__main__":
    app.run(debug=True)

