from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 데이터베이스 연결 URI 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://funcoding:funcoding@localhost/db_name'
# postgreSQL 사용시 아래의 코드를 사용
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://username:password@localhost/db_name'

# SQLAlchemy 인스턴스 초기화
db = SQLAlchemy(app)

# 데이터베이스 모델 정의
class User(db.Model):
    # 각 필드 정의
    id = db.Column(db.Integer, primary_key=True) # 사용자 ID, 기본 키로 설정
    username = db.Column(db.String(80), unique=True, nullable=False) # 사용자 이름, 중복 불가능 및 필수
    email = db.Column(db.String(120), unique=True, nullable=False) # 이메일 주소, 중복 불가능 및 필수

    def __repr__(self):
        return f'<User {self.username}>' # 객체를 문자열로 표현할 떄 사용할 양식
    
# 앱 컨텍스트 안에서 DB 테이블 생성
with app.app_context():
    db.create_all()

# 라우트 정의
@app.route('/')
def index():
    # 데이터 생성 (Create)
    new_user = User(username='john', email='john@exmaple.com')
    db.session.add(new_user)
    db.session.commit()

    # 데이터 조회 (Read)
    user = User.query.filter_by(username='john').first()

    # 데이터 업데이트 (Update)
    user.email = 'john@newexample.com'
    db.session.commit()

    # 데이터 삭제 (Delete)
    db.session.delete(user)
    db.session.commit()

    return 'CRUD operations completed'

# 테스트
# 사전 작업
"""
    데이터베이스 생성: 'db_name'에 해당하는 MySQL 데이터베이스가 생성되어 있어야 한다.
    적절한 데이터베이스 접속 설정: 각자의 환경에 맞추어 SQLALCHEMY_DATABASE_URI 기반 데이터베이스 접속 설정을 수정합니다.
"""
# 주요 코드 설명
"""
    데이터베이스 연결: 'SQLALCHEMY_DATABASE_URI' 설정을 통해 애플리케이션은 MySQL 데이터베이스에 연결됩니다. 
                    이번 코드에서는 데이터베이스 접속 사용자 이름과 비밀번호가 funcoding이고, 데이터베이스 이름은 db_name입니다.
    모델 정의: User 모델은 데이터베이스의 'users' 테이블을 나타냅니다. 각 필드 (id, username, email)와 그들의 제약 조건 (기본 키, 고유, 필수)이 정의되어 있습니다.
    테이블 생성: with app.app_context(): 구문을 통해 애플리케이션 컨텍스트 안에서 db.create_all()이 호출되어 정의된 모델에 따라 테이블이 데이터베이스에 생성됩니다.
"""
# 결과
"""
    데이터 생성(Create): 'john'이라는 username과 'john@example.com'이라는 email을 가진 새로운 User 객체가 생성되고, 데이터베이스에 커밋됩니다.
    데이터 조회(Read): username이 'john'인 User 객체를 조회합니다.
    데이터 업데이트(Update): 조회된 User 객체의 email을 'john@newexample.com'으로 변경하고 데이터베이스에 커밋합니다.
    데이터 삭제(Delete): 조회된 User 객체를 데이터베이스에서 삭제하고 커밋합니다.
    결과: 이 모든 CRUD 작업이 성공적으로 완료되면, 서버는 'CRUD operations completed'라는 메시지를 반환합니다.
    주의 사항: 위 코드는 한 번의 HTTP 요청으로 모든 CRUD 작업을 수행합니다. 실제 애플리케이션에서는 이러한 작업들을 개별적인 API 엔드포인트로 분리하여 처리하는 것이 일반적입니다.
                데이터 삭제가 포함되어 있기 때문에 이 URL을 한 번 요청할 때마다 'john' 사용자는 생성되고 삭제됩니다.
                따라서, 페이지를 새로고침할 때마다 'john' 사용자는 다시 생성되고 삭제됩니다.
"""