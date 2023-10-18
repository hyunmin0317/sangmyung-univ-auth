# sangmyung-univ-auth ![Python versions](https://img.shields.io/badge/Python-3.9-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Release](https://img.shields.io/badge/release-0.0.1-red)
### 상명대학교 재학생 인증 라이브러리

---

## Easy to install

**Pip**: `pip install sangmyung-univ-auth`

**Direct:**

- `git clone https://github.com/hyunmin0317/sangmyung-univ-auth`
- `python setup.py install`

## Easy to use

상명대학교 재학생 여부를 간편하게 확인하는 라이브러리입니다.<br>
재학생 인증 방식은 상명대학교 e-Campus 세션 인증 방식이며,<br>
해당 라이브러리 사용 방법은 아래와 같습니다.

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

### AuthResponse

인증 결과는 namedtuple 형태로 반환됩니다.

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
- **is_auth: 인증 성공 여부**
  - Type: bool
  - Value
    - True: 인증 성공
    - False: 인증 실패
- **code: Authenticator 반환 코드**
  - Type: str
  - Value
    - 'success': 인증에 성공할 경우
    - 'auth_failed': 인증에 실패할 경우
    - 'unknown_issue': 기타 라이브러리 오류
- **body: 메타데이터**
  - Type: dict 
  - Key
    - name: 이름
    - department: 학과
    - email: 이메일
