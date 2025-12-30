from flask import Flask, make_response

app = Flask(__name__)

# 기본 예제
@app.route('/response')
def response_example():
    # 응답 객체 생성, "Hello with header"는 응답 바디이며, 200은 HTTP 상태 코드
    response = make_response("Hello with header", 200)
    # 'Custom-Header'라는 이름의 사용자 정의 헤더를 설정하고 'custom_value'라는 값을 지정
    response.headers['Custom-Header'] = 'custom_value'
    # 응답 객체를 반환
    return response

# make_response 함수의 세 번째 인자로 headers를 전달하는 예제
@app.route('/direct')
def direct_response_example():
    # header 값 설정
    headers = {'X-Example' : 'DirectHeader'}
    return make_response("Direct Response", 200, headers)

# make_response 함수 호출 후 생성된 응답 객체에 .headers 속성을 사용하여 헤더를 추가하는 예제
@app.route('/custom')
def custom_response():
    response = make_response("Custom Response", 200)
    # 응답 객체의 headers 속성을 사용하여 'X-Example'라는 이름의 헤더를 추가하고 'CustomHeader'라는 값을 지정
    response.headers['X-Example'] = 'CustomHeader'
    return response
