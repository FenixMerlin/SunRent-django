# tasks.py
from apscheduler.schedulers.background import BackgroundScheduler
from Apps.models import Scooter, Polygon
from .pars import get_data
from .login import get_csrf_token, login
from django.contrib.gis.geos import Point  # Измените импорт
from requests import Session

import json

def update_scooters():
    session = Session()
    username = 'bishkek@sunrent.kg'
    password = '1234'
    token = get_csrf_token(session)
    
    if not login(session, username, password, token):
        print("Не удалось войти.")
        return
    
    data = {
        'car_group': '["0"]',
        'fuel': '{"from":"5","to":"30"}'
    }
    json_data = get_data(session, data)
    
    Scooter.objects.all().delete()

    if json_data and "data" in json_data:
        for item in json_data["data"]:
            identifier = item['scooter_id']
            battery_percentage = float(item['battery_percentage'])
            latitude = float(item['latitude'])
            longitude = float(item['longitude'])
            
            # Создаем объект Point с координатами и SRID
            location = Point(longitude, latitude, srid=4326)
            polygon = Polygon.objects.filter(area__contains=location).first()
            scooter, created = Scooter.objects.update_or_create(
                identifier=identifier,
                defaults={
                    'battery_percentage': battery_percentage,
                    'location': location,
                    'polygon': polygon
                }
            )
