import requests
from bs4 import BeautifulSoup as bs


def authenticate(username: str, password: str):
    with requests.session() as session:
        user_info = {'username': username, 'password': password}
        request = session.post('https://ecampus.smu.ac.kr/login/index.php', data=user_info)
        if request.url == 'https://ecampus.smu.ac.kr/':
            return session


def get_userinfo(session) -> dict:
    response = session.get('https://ecampus.smu.ac.kr/user/user_edit.php')
    soup = bs(response.text, 'html.parser')
    return {
        'name': soup.find('input', id='id_firstname').get('value'),
        'department': soup.find('input', id='id_department').get('value'),
        'email': soup.find('input', id='id_email').get('value')
    }
