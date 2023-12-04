import requests


def authenticate(username: str, password: str):
    with requests.session() as session:
        url = 'https://smsso.smu.ac.kr/Login.do'
        user_info = {'user_id': username, 'user_password': password}
        request = session.post(url, data=user_info)
        session.get('https://smul.smu.ac.kr/index.do')
        if request.url != url:
            return session


def get_data(session, username: str, url: str) -> dict:
    response = session.post(url, data={'@d#': '@d1#', '@d1#tp': 'dm', '_AUTH_MENU_KEY': 'usrCPsnlInfoUpd-STD', '@d1#strStdNo': username})
    return response.json()


def get_userinfo(session, username: str) -> dict:
    response = get_data(session, username, 'https://smul.smu.ac.kr/UsrSchMng/selectStdInfo.do')
    data = response['dsStdInfoList'][0]
    return {
        'name': data['NM_KOR'],
        'department': data['TMP_DEPT_MJR_NM'].split()[-1],
        'email': data['EMAIL']
    }


def get_courses(session, username: str) -> list:
    response = get_data(session, username, 'https://smul.smu.ac.kr/UsrRecMatt/list.do')
    return response['dsRecMattList']
