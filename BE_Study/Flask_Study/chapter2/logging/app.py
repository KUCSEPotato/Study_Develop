from flask import Flask
import logging

app = Flask(__name__)

# 로그 레벨을 DEBUG로 설정합니다.
app.logger.setLevel(logging.DEBUG)
# 로그를 파일로 저장합니다. 추가적으로 날짜와 시간, 로그 레벨도 포함하도록 합니다.
logging.basicConfig(filename='application.log', level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

@app.route('/')
def home():
    # 여기서 각기 다른 로그 레벨의 로그를 생성합니다.
    app.logger.debug('Debug level log') # 디버그 메시지
    app.logger.info('Info level log') # 정보 메시지
    app.logger.warning('Warning level log') # 경고 메시지
    app.logger.error('Error level log') # 에러 메시지
    app.logger.critical('Critical level log') # 크리티컬 메시지
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)