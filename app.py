from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
app = Flask()


def create_app():
    db.init_app()
    migrate.init_app()
    app.init_app()
