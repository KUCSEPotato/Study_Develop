from flask import Flask, request

app = Flask(__name__)

@app.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
def manage_user():
    if request.method == 'GET':
        return "Get user information"
    elif request.method == 'POST':
        return "Create a new user"
    elif request.method == 'PUT':
        return "Update user information"
    elif request.method == 'DELETE':
        return "Delete a user"
