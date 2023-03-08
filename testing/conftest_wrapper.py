from config import Config as dev_config
from app import create_app

def wrapper_client(branch):
    if branch == "dev":
        app_config = dev_config

    flask_app = create_app(app_config)
    testing_client = flask_app.test_client()

    return testing_client