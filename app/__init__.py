from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app(config):
    app = Flask(__name__)

    db.init_app(app)
    migrate.init_app(app)

    from app.resources import tag_bp, post_bp, comment_bp
    app.register_blueprint(tag_bp, url_prefix='/tags')
    app.register_blueprint(post_bp, url_prefix='/posts')
    app.register_blueprint(comment_bp, url_prefix='/comments')

    return app
