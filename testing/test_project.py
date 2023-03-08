#everythig needs to start with test_
from app.models import PostModel
import pytest
from app import create_app
from dotenv import load_dotenv
from config import Config

# def test_home(client):
#     response = client.get("/")
#     #b for bytes type
#     assert b"<title>Home</title>" in response.data

#testing based on what you expect to happen
#want app as arg because you need app context
def test_registration(client, app):
    response = client.post("/comments", data={"title":"Test post title","text":"Test post text"})

    with app.app_context():
        assert PostModel.query.count() == 1
        assert PostModel.query.first().title == "Test post title"
        assert PostModel.query.first().text == "Test post text"

