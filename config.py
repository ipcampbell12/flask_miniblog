import os
from dotenv import load_dotenv

load_dotenv()


class Config():
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
    PROPATAGE_EXCEPTIONS = True

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABSE_URL")
    SQLALCHEMY_TRACK_MODIFICATION = False
