from flask import Flask, jsonify, request

app = Flask(__name__)
user_data = {}

@app.route('/user/<username>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def manage_user(username):
    if request.method == 'GET':
        return jsonify({username: user_data.get(username, "User not found")})
    
    elif request.method == 'POST':
        new_data = request.json # JSON data expected
        user_data[username] = new_data
        return jsonify({username: new_data}), 201
    
    elif request.method == 'PUT':
        updated_data = request.json # JSON data expected
        if username in user_data:
            user_data[username].update(updated_data)
            return jsonify({username: user_data[username]})
        else:
            return jsonify({"error": "User not found"}), 404
        
    elif request.method == 'DELETE':
        if username in user_data:
            del user_data[username]
            return jsonify({"message": "User deleted"}), 200
        else:
            return jsonify({"error": "User not found"}), 404