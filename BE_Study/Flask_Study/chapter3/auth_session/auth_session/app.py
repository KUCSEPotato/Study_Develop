from flask import Flask, request, redirect, url_for, session # 웹 애플리케이션과 세션 관리
from flask_sqlalchemy import SQLAlchemy # 데이터베이스 ORM
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin, current_user # 사용자 인증 관리

# flask 애플리케이션 생성
app = Flask(__name__)
# DB 설정을 애플리케이션 설정에 추가, 현재는 MySQL 데이터베이스를 사용
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/flask_study'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'my_secret_key'  # 세션 암호화 키 설정

# SQLAlchemy 객체 생성, 애플리케이션에 바인딩
db = SQLAlchemy(app)

# 로그인 관리자 인스턴스 생성
login_manager = LoginManager()
# 로그인 관리자 초기화, 애플리케이션에 바인딩
login_manager.init_app(app)
# 로그인 페이지 설정
login_manager.login_view = 'login'

# 데이터베이스 모델을 정의, UserMixin을 상속받아 사용자 모델 생성
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 사용자 ID
    username = db.Column(db.String(150), unique=True, nullable=False)  # 사용자 이름
    email = db.Column(db.String(150), unique=True, nullable=False)  # 이메일
    password = db.Column(db.String(150), nullable=False)  # 비밀번호

    # 객체의 문자열 표현을 정의
    def __repr__(self):
        return f'<User {self.username}>'
    
# 사용자 ID로 사용자를 로드하는 콜백 함수 정의
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# DB 테이블 생성
with app.app_context():
    db.create_all()

# 인덱스 뷰 정의, '/' 경로에 접근 시 호출
@app.route('/')
def index():
    user_id = session.get('user_id') # 세션에서 user_id 가져오기
    if user_id:
        user = User.query.get(user_id)
        return f'Hello, {user.username}!'
    return 'You are not Logged in.'

# 보호된 페이지를 위한 뷰를 정의.
@app.route('/protected')
@login_required
def protected():
    return f'Welcome to the protected page, {current_user.username}!'

# 로그인 뷰 정의, '/login' 경로에 접근 시 호출, GET과 POST 메소드 지원
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # DB에서 사용자 조회
        user = User.query.filter_by(username=username).first()
        # 사용자가 존재하고 비밀번호가 맞을 경우
        if user and user.password == password:
            login_user(user)
            session['user_id'] = user.id
            return redirect(url_for('protected'))  # 보호된 페이지로 리다이렉트
        
    # 로그인 폼 렌더링
    return """
    <form method="POST">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    """

# 로그아웃 뷰를 정의
@app.route('/logout')
@login_required # 로그인이 필요하다는 데코레이터
def logout():
    logout_user() # 사용자 로그아웃
    session.pop('user_id', None) # 세션에서 user_id 제거
    return redirect(url_for('index')) # 인덱스 페이지로 리다이렉트

# 테스트 사용자를 생성하는 뷰를 정의
@app.route('/create_test_user')
def create_test_user():
    test_user = User(username='testuser', email='test@example.com', password='testpassword')
    db.session.add(test_user)
    db.session.commit()
    return 'Test user created!'

