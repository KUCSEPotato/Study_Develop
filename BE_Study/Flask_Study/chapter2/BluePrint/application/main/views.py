from flask import Flask, Blueprint

# Blueprint 생성
main_blueprint = Blueprint('main', __name__)

# 블루프린트에 라우트 정의
@main_blueprint.route('')
def home():
    return "Home Page"

# 블루프린트를 Flask 애플리케이션에 등록하는 과정은 app.py에서 진행됩니다.
