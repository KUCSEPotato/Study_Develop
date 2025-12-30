from flask import Flask, request, jsonify

app = Flask(__name__)

# query parameter example, request.args is used to access query parameters
@app.route('/query')
def query_example():
    language = request.args.get('language')
    return f"Requested language: {language}"

# json body example, repense with JSON data
@app.route('/json')
def json_example():
    # jsonify를 사용하여 JSON 형식의 응답을 반환
    return jsonify({"message": "Hello, JSON!"})
