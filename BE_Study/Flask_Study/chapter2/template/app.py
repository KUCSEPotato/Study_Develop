from flask import Flask, render_template

app = Flask(__name__)
@app.route('/hello/<name>')
def hello_name(name):
    # render_template 함수를 사용하여 templates 폴더 내의 hello.html 파일을 렌더링
    # name 변수를 템플릿에 전달
    return render_template('hello.html', name=name)

# fruits_list.html 파일을 렌더링하는 라우트
@app.route('/fruits')
def show_fruits():
    fruits = ['apple', 'banana', 'cherry']
    return render_template('fruits_list.html', fruits=fruits)

@app.route('/messages')
def show_message():
    return render_template('messages.html')