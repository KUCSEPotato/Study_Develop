from flask import Flask, Blueprint

# app = Flask(__name__)은 여기서 필요하지 않습니다.
# 그 이유는 이 파일이 블루프린트 정의만을 포함하고 있기 때문입니다.
# 위의 코드는 app.py 파일에서만 작성하면 됩니다. 메인 애플리케이션에서만 작성합니다.

# Blueprint 생성
auth_blueprint = Blueprint('auth', __name__)

# 블루프린트에 라우트 정의
@auth_blueprint.route('/login')
def login():
    return "Login Page"

@auth_blueprint.route('/logout')
def logout():
    return "Logout Page"

# 블루프린트를 Flask 애플리케이션에 등록하는 과정은 app.py에서 진행됩니다.
