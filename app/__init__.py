from flask import Flask

import app.extensions as ex
import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)

    ex.db.init_app(app)
    ex.login_manager.init_app(app)

    from app.models import User
    @ex.login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    from app.routes import auth, blog, portfolio

    app.register_blueprint(portfolio.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(auth.bp)

    return app
