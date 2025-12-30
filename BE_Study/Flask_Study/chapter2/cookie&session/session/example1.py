from flask import Flask, session

app = Flask(__name__)
# 여기서 'your_secret_key'는 실제로는 안전하게 관리되어야 하는 민감한 정보입니다.
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return "Welcome to the Session Example!"

# 세션 데이터 설정 라우트
@app.route('/set_session')
def set_session():
    session['username'] = 'potato'
    return "Session variable 'username' set to 'potato'!"

# 세션 데이터 가져오기 라우트
@app.route('/get_session')
def get_session():
    username = session.get('username')

    if username:
        return f"Hello, {username}!"
    else:
        return "Hello, Guest!"
