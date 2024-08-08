from django.contrib.gis.geos import Point
from Apps.models import*

def process_data(data):
    if not data:
        print("Нет данных для обработки.")
        return

    for item in data:
        scooter_id = item['scooter_id']
        battery_percentage = float(item['battery_percentage'])
        latitude = float(item['latitude'])
        longitude = float(item['longitude'])
        location = Point(x = longitude, y = latitude)

        # Найти полигон, в который попадает местоположение самоката
        polygon = Polygon.objects.filter(area__contains=location).first()

        # Если полигон найден, сохраняем самокат
        if polygon:
            Scooter.objects.update_or_create(
                identifier=scooter_id,
                defaults={
                    'location': location,
                    'battery_percentage': battery_percentage,
                    'polygon': polygon
                }
            )
        else:
            print(f"Полигон для самоката {scooter_id} не найден.")
