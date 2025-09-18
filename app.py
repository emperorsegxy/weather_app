from flask import Flask, render_template, request
from waitress import serve
from weather import get_current_weather
import logging

import json


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/weather', methods=['POST'])
def get_weather_data():
    city = request.form.get('city')
    device_info = request.form.get('device_info')
    try:
        device_info = json.loads(device_info)
    except:
        logging.warn("Could not convert from JSON")
    logging.info(device_info)
    logging.info(city)
    weather_data = get_current_weather(city)
    logging.info(weather_data)
    if weather_data is None:
        return render_template("city_not_found.html", weather={'city': city})
    # return
    weather = {
        'title': weather_data['name'],
        'city': weather_data['name'],
        'temperature': f"{weather_data['main']['temp']:.1f}",
        'feels_like': f"{weather_data['main']['feels_like']}",
        'description': weather_data['weather'][0]['description'].capitalize()
    }
    return render_template("weather_display.html", weather=weather)

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000, _quiet=False)