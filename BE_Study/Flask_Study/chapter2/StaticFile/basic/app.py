from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# 메인 페이지 라우트
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/image')
def get_image():
    return send_from_directory(app.static_folder, 'image.jpg')