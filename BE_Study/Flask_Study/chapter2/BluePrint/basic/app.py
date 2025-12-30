from flask import Flask, Blueprint

app = Flask(__name__)

# Blueprint 객체 생성
# 첫 번째 인자는 블루프린트의 이름
# 두 번째 인자는 블루프린트가 속한 모듈 또는 패키지의 이름, 일반적으로 '__name__'을 사용
auth_blueprint = Blueprint('auth', __name__)

# 블루프린트를 사용하여 라우트 정의
@auth_blueprint.route('/login')
def login():
    return "Login Page"

@auth_blueprint.route('/logout')
def logout():
    return "Logout Page"

# 블루프린트를 Flask 애플리케이션에 등록
# url_prefix는 블루프린트의 URL 경로 앞에 추가되는 접두사
app.register_blueprint(auth_blueprint, url_prefix='/auth')