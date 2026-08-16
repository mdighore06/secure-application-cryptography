import os
from dotenv import load_dotenv

# Load configuration from environment variables (.env)
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "default-dev-key-change-in-production")
DB_URI = os.getenv("DB_URI", "sqlite:///app.db")
API_CREDENTIAL = os.getenv("API_CREDENTIAL")
