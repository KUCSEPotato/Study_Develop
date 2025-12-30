from flask import Flask, url_for, redirect
app = Flask(__name__)

# 홈페이지
@app.route('/')
def index():
    # 여기서는 url_for('index')를 호출합니다.
    return f'홈 페이지: {url_for("index")}'

# 사용자 프로필 페이지
@app.route('/user/<username>')
def user_profile(username):
    # 여기서는 url_for('user_profile', username=username)를 호출합니다.
    return f'사용자 {username}의 프로필 페이지: {url_for("user_profile", username=username)}'

# 정적 파일 테스트를 위한 경로
@app.route('/static-example')
def static_example():
    # 여기서는 url_for('static', filename='style.css')를 호출합니다.
    return f'정적 파일 경로: {url_for("static", filename="style.css")}'

# 절대 URL 테스트
@app.route('/absolute')
def absolute():
    # 여기서는 url_for('index', _external=True)를 호출합니다.
    return f'외부 절대 URL: {url_for("index", _external=True)}'

# HTTPS와 절대 URL 테스트
@app.route('/https')
def https():
    # 여기서는 url_for('index', _external=True, _scheme='https')를 호출합니다.
    return f'HTTPS 절대 URL: {url_for("index", _external=True, _scheme="https")}'
