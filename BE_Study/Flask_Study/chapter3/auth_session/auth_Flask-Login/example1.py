# pip install Flask-Login
from flask_login import LoginManager

# LoginManager 인스턴스 생성
login_manager = LoginManager()
# Flask 애플리케이션과 인스턴스 연결
login_manager.init_app(app)

"""
LoginManager 클래스는 사용자의 로그인 상태를 관리하기 위한 여러 메서드와 속성을 제공합니다.
login_manager.init_app(app) 메서드를 통해 Flask 애플리케이션과 LoginManager 인스턴스를 연결합니다.
이렇게 하면 Flask 애플리케이션에서 로그인 관련 기능을 사용할 수 있게 됩니다.
"""

from flask_login import UserMixin

class User(UserMixin, db.Model):
    # 각 컬럼 정의
    id = db.Column(db.Integer, primary_key=True)  # 사용자 ID, 기본 키로 설정
    username = db.Column(db.String(80), unique=True, nullable=False)  # 사용자 이름, 중복 불가능 및 필수
    password = db.Column(db.String(200), nullable=False)  # 비밀번호, 필수

"""
UserMixin 클래스는 Flask-Login에서 제공하는 클래스로, 로그인 관리에 필요한 메서드를 포함합니다.
이 클래스는 데이터베이스 모델이면서 UserMixin을 상속받아 Flask-Login과 호환됩니다.
"""

# 사용자 로드 함수에 데코레이터 적용
@login_manager.user_loader
def load_user(user_id):
    # 사용자 ID를 기반으로 데이터베이스에서 사용자 객체를 조회
    return User.query.get(int(user_id))

# @login_manager.user_loader 데코레이터는 Flask-Login이 사용자 객체를 로드할지 알려줍니다.
# load_user 함수는 사용자 ID를 인자로 받아 해당 ID에 해당하는 사용자 객체를 데이터베이스에서 조회합니다.
# Flask-Login은 사용자 관리를 위해 이 함수를 내부적으로 사용합니다. 

# 전체적인 흐름을 정리하자면 다음과 같습니다.
# 1. 플라스크 애플리케이션이 시작할 때, LoginManager 인스턴스를 초기화하고 플라스크 애플리케이션에 등록합니다.
# 2. 사용자 클래스를 정의하며, 이 클래스는 로그인 관리를 위해 UserMixin을 상속받습니다.
# 3. 사용자 ID를 받아 데이터베이스에서 해당 사용자를 찾아 반환하는 load_user 함수를 정의합니다.
# 4. @login_manager.user_loader 데코레이터는 Flask-Login에게 사용자 로딩 메커니즘을 제공합니다.

