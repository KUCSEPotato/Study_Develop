from flask import Flask, url_for

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

# 예제 1
# 기본 홈페이지 경로
@app.route("/")
def index():
    return '홈페이지에 오신 것을 환영합니다!'

# 사용자 정보 페이지 경로
@app.route("/user/<username>")
def profile(username):
    # url_for 함수를 사용하여 'index' 뷰 함수의 URL을 생성
    return f'사용자 {username}의 프로필 페이지입니다. 홈으로 가기: {url_for("index")}'

# 예제 2
@app.route('/home')
def home():
    return '홈페이지에 오신 것을 환영합니다!.'

@app.route('/user/<username>')
def user_profile(username):
    return f'사용자 {username}의 프로필 페이지입니다. 홈으로 가기: {url_for("index")}'