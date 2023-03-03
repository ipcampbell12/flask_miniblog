from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app,db)

    from .resources.tag_resource import tag_bp
    app.register_blueprint(tag_bp, url_prefix='/tags')

    from .resources.post_resource import post_bp
    app.register_blueprint(post_bp, url_prefix='/posts')

    from .resources.comment_resource import comment_bp
    app.register_blueprint(comment_bp, url_prefix='/comments')

    return app
#have to import models - remove this and see if migration worked
from app import models
