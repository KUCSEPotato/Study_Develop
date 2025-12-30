from flask import Flask, make_response, request, abort

app = Flask(__name__)

@app.route('/')
def main():
    return f"main homepage"

@app.route('/set_cookie')
def set_cookie():
    resp = make_response('쿠키를 설정합니다.')
    resp.set_cookie('username', 'potato')
    return resp

@app.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('username', 'Geust')
    return f"쿠키로 부터 얻은 사용자 이름: {username}"

@app.route('/secret')
def secret():
    username = request.cookies.get('username')
    if not username:
        # 쿠키가 없다면 접근 금지 메시지 반환
        abort(403, description="접근 권한이 없습니다. 먼저 쿠키를 설정해주세요.")
    else:
        return f"환영합니다, {username}님! 비밀 페이지에 접속하셨습니다."

# 쿠키 삭제 라우트    
@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response('쿠키를 삭제합니다.')
    resp.delete_cookie('username')
    return resp

# set_cookie에 사용할 수 있는 option들 보충 설명
"""
# max_age 옵션은 쿠키가 유지될 시간을 초 단위로 설정합니다.
resp.set_cookie('username', 'potato', max_age = 60 * 60 * 24 * 7)

# expires 옵션은 쿠키가 만료되는 정확한 날짜와 시간을 설정할 수 있습니다.
resp.set_cookie('username', 'potato', expires = datetime.datetime(2027, 11, 7))

# path 옵션을 통해 쿠키의 유효 경로를 제한할 수 있습니다. 
# 아래 코드는 '/app' 경로와 이 경로의 하위 경로에서만 쿠키가 유효하게 됩니다.
# 쿠키는 기본적으로 도메인의 모든 경로에 대해 유효합니다. (pate='/')
resp.set_cookie('username', 'potato', path = '/app')

# domain 옵션을 설정하면 쿠키가 특정 도메인에서 유효하게 됩니다.
# 서브 도메인 간에 쿠키를 공유할 수 있습니다.
resp.set_cookie('username', 'potato', domain='.example.code')

# secure 옵션이 True로 설정되면, 쿠키는 HTTPS 연결을 통해서만 전송됩니다.
resp.set_cookie('username', 'potato', secure=True)

# httponly 옵션을 True로 설정하면, 쿠키는 웹 서버를 통해서만 접근할 수 있습니다. 
resp.set_cookie('username', 'potato', httponly=True)
"""