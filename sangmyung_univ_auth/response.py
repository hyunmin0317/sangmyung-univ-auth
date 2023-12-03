from collections import namedtuple

AuthResponse = namedtuple(
    'AuthResponse', [
        'is_auth',      # bool or None: 인증 여부
        'code',         # str: 반환 코드
        'body'          # Any: 메타데이터
    ]
)


def _success(body=None):
    return AuthResponse(
        is_auth=True,
        code='success',
        body=body or {}
    )


def _auth_failed():
    return AuthResponse(
        is_auth=False,
        code='auth_failed',
        body={'message': '아이디 및 비밀번호가 일치하지 않습니다.'}
    )


def _unknown_issue():
    return AuthResponse(
        is_auth=None,
        code='unknown_issue',
        body={
            'message': '모듈이 예상한 포맷과 다릅니다. 관리자에게 문의해주세요! '
                       '[https://github.com/hyunmin0317/sangmyung-univ-auth/issues]'
        }
    )
