import requests


def authenticate(username: str, password: str):
    with requests.session() as s:
        url = 'https://smsso.smu.ac.kr/Login.do'
        user_info = {'user_id': username, 'user_password': password}
        request = s.post(url, data=user_info)
        s.get('https://smul.smu.ac.kr/index.do')
        if request.url == url:
            return
        return s, username


def get_userinfo(session) -> dict:
    session, username = session
    response = session.post('https://smul.smu.ac.kr/UsrSchMng/selectStdInfo.do', data={'@d#': '@d1#', '@d1#tp': 'dm', '_AUTH_MENU_KEY': 'usrCPsnlInfoUpd-STD', '@d1#strStdNo': username})
    data = response.json()['dsStdInfoList'][0]
    return {
        'name': data['NM_KOR'],
        'department': data['TMP_DEPT_MJR_NM'].split()[-1],
        'email': data['EMAIL']
    }


def get_courses(session) -> list:
    session, username = session
    response = session.post('https://smul.smu.ac.kr/UsrRecMatt/list.do', data={'@d#': '@d1#', '@d1#tp': 'dm', '_AUTH_MENU_KEY': 'usrCPsnlInfoUpd-STD', '@d1#strStdNo': username})
    return response.json()['dsRecMattList']
