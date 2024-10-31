from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='your_secret_key',
    )

    from . import auth, blog
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)

    return app