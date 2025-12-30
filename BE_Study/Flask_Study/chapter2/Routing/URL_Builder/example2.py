from flask import Flask, url_for

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

@app.route('/user/<username>')
def show_user_profile(username):
    # 실제로는 사용자 프로필 정보를 보여주는 로직이 위치
    return f'User {username}'

# 뷰 함수: 게시물을 보여주는 함수
@app.route('/post/<year>/<month>/<day>')
def show_post(year, month, day):
    # 실제로는 게시물 정보를 보여주는 로직이 위치
    return f'Post published on {year}/{month}/{day}'

# 홈페이지에서 url_for를 이용하여 위의 뷰 함수들로 이동하는 링크를 생성
@app.route('/')
def index():
    # 'show_user_profile_url' 뷰로 이동하는 URL 생성
    user_url = url_for('show_user_profile', username='potato')
    # 'show_post' 뷰로 이동하는 URL 생성
    post_url = url_for('show_post', year='2025', month='06', day='30')
    # 생성된 url 반환
    return f'<a href="{user_url}">User Profile</a><br>' \
           f'<a href="{post_url}">Post</a>'

"""
# url_for()
The `url_for()` function in Flask is used to generate URLs for specific view functions. 
It takes the name of the view function as its first argument and any variable arguments that the view function requires. 
This is particularly useful for creating links to routes dynamically, ensuring that the URLs are always correct even if the route definitions change.

# grammar:
    url_for(view_function_name): 
    뷰 함수의 이름을 기반으로 해당 뷰 함수에 매핑된 URL을 반환 
    
    url_for('view_function_name', **values): 
    뷰 함수에 전달되어야 하는 변수들을 values에 '변수 = 변숫값 형태 (eg. user_id = 123, username = 'potato')로 전달하면 해당 변수들을 포함한 URL을 생성
"""