from flask import Flask, render_template

app = Flask(__name__)

@app.route("/about")
def about_page():
    # 'render_template' 함수를 사용하여 'about.html' 파일을 렌더링
    # 플라스크는 'about.html' 파일과 함께 이 템플릿이 상속하는 모든 부모 템플릿 (base.html 포함)을 렌더링하여 최종 HTML을 생성합니다.
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
