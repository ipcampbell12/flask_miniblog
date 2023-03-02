from app import create_app
from dotenv import load_dotenv
from config import Config


app = create_app(Config)

if __name__ == 'main':
    app.run(debug=True)
