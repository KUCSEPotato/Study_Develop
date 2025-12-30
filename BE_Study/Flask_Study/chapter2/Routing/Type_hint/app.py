from flask import Flask

app = Flask(__name__)

@app.route('/int/<int:var>')
def int_route(var: int) -> str:
    return f'정수: {var}'

@app.route('/float/<float:var>')
def float_route(var: float) -> str:
    return f'실수: {var}'

@app.route('/path/<path:var>')
def path_route(var: str) -> str:
    return f'경로: {var}'

@app.route('/uuid/<uuid:var>')
def uuid_route(var: str) -> str:
    return f'UUID: {var}'
