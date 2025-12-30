from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin, current_user

app = Flask(__name__)

# 데이터베이스 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://funcoding:funcoding@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'PotaoGoat'

db = SQLAlchemy(app) # SQLAlchemy 객체 생성

login_manager = LoginManager() # Flask-Login의 LoginManager 객체 생성
login_manager.init_app(app) # 어플리케이션에 LoginManager 적용
login_manager.login_view = 'login' # 로그인 페이지의 뷰 함수 이름을 설정

# 사용자 모델 정의
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
# 애플리케이션 컨텍스트 안에서 데이터베이스 테이블 생성
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) # 주어진 사용자 ID에 해당하는 사용자 객체를 반환

@app.route('/')
@login_required # 로그인된 사용자만 액세스 가능
def index():
    return 'Hello, World!'

@app.route('/protected')
@login_required # 로그인된 사용자만 액세스 가능
def protected():
    return f'Hello, {current_user.username}! This is a protected route.' # 현재 로그인한 사용자의 이름을 표시

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first() # 데이터베이스에서 사용자 조회

        if user and user.password == password:
            login_user(user) # 사용자가 존재하고 비밀번호가 맞다면 로그인 처리
            return redirect(url_for('protected')) # 보호된 페이지로 리다이렉트
        # 로그인 폼 HTML 반환, 사실 templalte으로 하는게 좋아보이긴 함.
    return '''
    <form method="POST">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/logout')
@login_required # 로그인된 사용자만 액세스 가능
def logout():
    logout_user() # 현재 사용자 로그아웃 처리
    return redirect(url_for('index')) # 홈페이지로 리디렉션

@app.route('/crearte_test_user')
def create_test_user():
    # 테스트용 사용자 생성
    test_user = User(username='testuser', email='testuser@example.com', password='testpassword')
    db.session.add(test_user)
    db.session.commit() # 데이터베이스에 테스트 사용자 추가
    return 'Test user created successfully!' # 사용자 생성 완료 메시지 반환
