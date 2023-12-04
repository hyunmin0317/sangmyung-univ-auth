from sangmyung_univ_auth.authenticator import authenticate, get_userinfo
from sangmyung_univ_auth.response import AuthResponse, _auth_failed, _success, _unknown_issue


def auth(username: str, password: str) -> AuthResponse:
    try:
        session = authenticate(username, password)
        if not session:
            return _auth_failed()
        userinfo: dict = get_userinfo(session, username)
        return _success(body=userinfo)
    except Exception:
        return _unknown_issue()
