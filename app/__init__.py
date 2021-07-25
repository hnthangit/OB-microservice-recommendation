from flask import Flask


def create_app(test_config=None, **kwargs):
    app = Flask(__name__, **kwargs)

    from . import extensions

    from . import modules

    return app
