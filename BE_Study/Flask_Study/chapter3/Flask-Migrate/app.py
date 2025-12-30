# pip install Flask-Migrate
"""
초기 설정: flask db init 명령으로 마이그레이션 환경을 초기화, 실행하면 migrations 폴더가 생성됩니다. 이후 이 폴더 내에 마이그레이션 파일들이 저장됩니다.
마이그레이션 파일 생성: flask db migrate -m "Initial migration." 명령으로 현재 모델 상태를 기반으로 마이그레이션 파일을 생성합니다.
                    모델에 변경사항이 생기면, 이 변경 사항을 적용하기 위한 마이그레이션 파일을 생성해야 합니다.
                    위 명령은 migrations 폴더에 새로운 마이그레이션 파일을 생성합니다. -m 옵션ㅇㄴ 해당 마이그레이션에 대한 메시지를 추가하는 것입니다.
                    git commit -m "Initial migration"과 유사합니다.
마이그레이션 적용: flask db upgrade 명령으로 데이터베이스에 마이그레이션을 적용합니다. 이 명령은 migrations 폴더 내의 마이그레이션 파일을 읽고, 데이터베이스 스키마를 업데이트합니다.
롤백: 만약 마이그레이션을 되돌리고 싶다면, flask db downgrade 명령을 사용합니다. 이 명령은 이전 상태로 데이터베이스를 되돌립니다.
    참고로, 특정 버전의 데이터베이스로 되돌리고 싶다면, flask db downgrade <version> 명령을 사용합니다. 여기서 <version>은 되돌리고 싶은 마이그레이션 파일의 버전입니다.
    일반적으로 migrations/versions 디렉토리에 각 마이그레이션 버전이 저장되어 있습니다.
    실제 사용 예시는 다음과 같습니다. flask db downgrade 1234567890ab
    다만, 롤백 명령은 테이블 구조를 이전 상태로 되돌릴 뿐, 데이터에 대해서는 롤백을 진행하지 않기 때문에 주의해야합니다.
    따라서, 롤백을 진행하기 전에 데이터 백업을 권장합니다.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://funcoding:funcoding@localhost/db_name'
db = SQLAlchemy(app)

# 모델 class 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User %r>' % self.username
    
# Flask-Migrate 초기화
migrate = Migrate(app, db)

if __name__ == '__main__':
    # 앱 컨텍스트 안에서 DB 테이블 생성
    with app.app_context():
        db.create_all()
    app.run(debug=True)