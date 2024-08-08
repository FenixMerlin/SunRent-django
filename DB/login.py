from bs4 import BeautifulSoup

# URLs для запроса данных и загрузки файла
login_url = "https://sunrent-kg.bumerang.tech/admin/login"

# Получение CSRF токена
def get_csrf_token(session):
    response = session.get(login_url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    meta_tag = soup.find('meta', {'name': 'csrf-token'})
    
    if meta_tag and 'content' in meta_tag.attrs:
        return meta_tag['content']
    else:
        print("Токен не найден на странице")
        return None

# Вход на сайт
def login(session, username, password, token):
    login_data = {
        'username': username,
        'password': password,
        '_token': token
    }

    response = session.post(login_url, data=login_data)
    response.raise_for_status()
    
    if response.status_code == 200:
        return True
    else:
        return False
