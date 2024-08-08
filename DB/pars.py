import requests
import json
from bs4 import BeautifulSoup
from .login import*

data_url = "https://sunrent-kg.bumerang.tech/admin/car/search"

def clean_html(html):
  soup = BeautifulSoup(html, 'html.parser')
  return soup.get_text(strip=True)

def get_data(session, data):
  token = get_csrf_token(session)
  
  if not token:
    print("CSRF токен не найден.")
    return None
  
  headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari53736',
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRF-TOKEN': token,
    'Referer': 'https://sunrent-kg.bumerang.tech/admin/car',
    'Origin': 'https://sunrent-kg.bumerang.tech'
  }
  
  try:
    response = session.post(data_url, headers=headers, data=data)
    response.raise_for_status()
    
    json_data = response.json()
    
    # Очистка данных в поле "data" и извлечение нужных значений
    if "data" in json_data:
      extracted_data = []
      for row in json_data["data"]:
          if len(row) >= 4:  # Убедитесь, что достаточно данных
              scooter_id = clean_html(row[1])
              battery_percentage = clean_html(row[8]).replace('%', '')  # Удаляем знак '%'
              latitude = clean_html(row[24])
              longitude = clean_html(row[25])
              extracted_data.append({
                  'scooter_id': scooter_id,
                  'battery_percentage': battery_percentage,
                  'latitude': latitude,
                  'longitude': longitude
              })

      
      json_data["data"] = extracted_data
    
    with open('DB/json/response_data.json', 'w', encoding='utf-8') as f:
      json.dump(json_data, f, ensure_ascii=False, indent=4)
    
    return json_data
  except requests.RequestException as e:
    print(f"Ошибка запроса: {e}")
    return None, "Ошибка", "Ошибка"