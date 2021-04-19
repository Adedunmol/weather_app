from flask import Blueprint, render_template, request
import requests
from .models import City
from website import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        new_city = request.form.get('city')
        if new_city:
            new_city_obj = City(name=new_city)
            db.session.add(new_city_obj)
            db.session.commit()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=ebbf86a5582d08b52b02283ffa6fb079'

    cities = City.query.all()

    weather_data = []

    for city in cities:
        name = city.name
        r = requests.get(url.format(name)).json()

        weather = {
                'city': city.name,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }
        weather_data.append(weather)

    return render_template('home.html', weather_data=weather_data)
