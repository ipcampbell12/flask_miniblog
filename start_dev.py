from app import create_app
from dotenv import load_dotenv


app = create_app()

if __name__ == 'main':
    app.run(debug=True)
