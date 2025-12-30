from flask import Flask, request
app = Flask(__name__)

# python3 app.py 명령어를 위한 코드
if __name__ == '__main__':
    app.run()

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Process the login form
        return "Login successful"
    else:
        # Show the login form
        return "Please log in"
    