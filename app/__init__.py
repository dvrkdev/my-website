from flask import Flask

import app.extensions as ex
import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)

    ex.db.init_app(app)

    # test the SECRET_KEY
    print(" * SECRET_KEY (worked):", app.secret_key)

    return app
