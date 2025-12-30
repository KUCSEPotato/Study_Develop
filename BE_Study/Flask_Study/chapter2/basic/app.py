from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# debug 설정은 실제 배포시에는 보안 상의 문제가 생길 수 있으므로 false로 설정
if __name__ == '__main__':
    app.run(debug=True)

# app.py 파일을 실행하면 Flask 서버가 시작됩니다.

    # @setupmethod
    # def route(self, rule: str, **options: t.Any) -> t.Callable[[T_route], T_route]:
    #     """Decorate a view function to register it with the given URL
    #     rule and options. Calls :meth:`add_url_rule`, which has more
    #     details about the implementation.

    #     .. code-block:: python

    #         @app.route("/")
    #         def index():
    #             return "Hello, World!"

    #     See :ref:`url-route-registrations`.

    #     The endpoint name for the route defaults to the name of the view
    #     function if the ``endpoint`` parameter isn't passed.

    #     The ``methods`` parameter defaults to ``["GET"]``. ``HEAD`` and
    #     ``OPTIONS`` are added automatically.

    #     :param rule: The URL rule string.
    #     :param options: Extra options passed to the
    #         :class:`~werkzeug.routing.Rule` object.
    #     """

    #     def decorator(f: T_route) -> T_route:
    #         endpoint = options.pop("endpoint", None)
    #         self.add_url_rule(rule, endpoint, f, **options)
    #         return f

    #     return decorator