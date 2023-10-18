import requests
from bs4 import BeautifulSoup as bs


def session_request(username: str, password: str):
    with requests.session() as s:
        user_info = {"username": username, "password": password}
        request = s.post("https://ecampus.smu.ac.kr/login/index.php", data=user_info)
        if request.url == "https://ecampus.smu.ac.kr/":
            return s
        return


def get_userinfo(session) -> dict:
    request = session.get("https://ecampus.smu.ac.kr/user/user_edit.php")
    source = request.text
    soup = bs(source, "html.parser")
    return {
        "name": soup.find('input', id='id_firstname').get('value'),
        "department": soup.find('input', id='id_department').get('value'),
        "email": soup.find('input', id='id_email').get('value')
    }
