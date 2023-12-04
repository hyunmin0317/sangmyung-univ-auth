from sangmyung_univ_auth.authenticator import authenticate, get_userinfo, get_courses
from sangmyung_univ_auth.response import AuthResponse, _auth_failed, _success, _unknown_issue


def process(username: str, password: str, func) -> AuthResponse:
    try:
        session = authenticate(username, password)
        return _success(body=func(session, username)) if session else _auth_failed()
    except Exception:
        return _unknown_issue()


def auth(username: str, password: str) -> AuthResponse:
    return process(username, password, get_userinfo)


def completed_courses(username: str, password: str) -> AuthResponse:
    return process(username, password, get_courses)
