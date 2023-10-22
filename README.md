# sangmyung-univ-auth ![Python versions](https://img.shields.io/badge/Python-3.9-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Release](https://img.shields.io/badge/release-1.0.2-red)
**상명대학교 재학생 인증 라이브러리**

## Features
- 상명대학교 재학생 여부를 간편하게 확인하는 라이브러리입니다.
- 재학생 인증 방식은 상명대학교 e-Campus 세션 인증 방식입니다.

## Easy to install
**Pip**: `pip install sangmyung-univ-auth`

**Direct:**
- `git clone https://github.com/hyunmin0317/sangmyung-univ-auth`
- `python setup.py install`

## Easy to use
```python
>>> from sangmyung_univ_auth import auth
>>> result = auth('201911019', '<my-password>')
>>> result
AuthResponse(is_auth=True, code='success', body={'name': '최현민', 'department': '컴퓨터과학전공', 'email': 'choihm9903@naver.com'})
>>> result.is_auth
True
>>> result.code
'success'
>>> result.body
{'name': '최현민', 'department': '컴퓨터과학전공', 'email': 'choihm9903@naver.com'}
```

## AuthResponse
```python
AuthResponse(
  is_auth=True,
  code='success',
  body={
    'name': '최현민', 
    'department': '컴퓨터과학전공', 
    'email': 'choihm9903@naver.com'
  }
)
```

- **is_auth**: 인증 성공 여부
  - Type: bool
  - Value
    - True: 인증 성공
    - False: 인증 실패
- **code**: Authenticator 반환 코드
  - Type: str
  - Value
    - 'success': 인증에 성공할 경우
    - 'auth_failed': 인증에 실패할 경우
    - 'unknown_issue': 기타 라이브러리 오류
- **body**: 메타데이터
  - Type: dict 
  - Key
    - name: 이름
    - department: 학과
    - email: 이메일

## Sangmyung University Auth API

- **Request**
  - **URL**
    ```text 
    https://smunity.co.kr/api/auth
    ```
  - **Method**
    `POST`
  - **Body**
    ```json
    {
        "username": "<학번>",
        "password": "<비밀번호>"
    }
    ```

- **Response**
  - **Success**: 200 OK
    ```json
    {
        "is_auth": true,
        "code": "success",
        "body": {
            "name": "최현민",
            "department": "컴퓨터과학전공",
            "email": "choihm9903@naver.com"
        }
    }
    ```
  - **Fail**: 401 Unauthorized
    ```javascript
    {
        "is_auth": false,
        "code": "auth_failed",
        "body": {
            "message": "아이디 및 비밀번호가 일치하지 않습니다."
        }
    }
    ```

## References
- https://github.com/hyunmin0317/sangmyung-univ-auth
- https://pypi.org/project/sangmyung-univ-auth/
- https://smunity.co.kr/api/auth
