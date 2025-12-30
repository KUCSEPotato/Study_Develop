from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def my_api():
    data = {
        'message': 'Hello, World!',
        'status': 'success'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)