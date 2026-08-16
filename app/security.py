import os
from dotenv import load_dotenv

# Load runtime environment configurations from local .env file
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DB_URI = os.getenv("DB_URI", "sqlite:///app.db")
API_CREDENTIAL = os.getenv("API_CREDENTIAL")

if not SECRET_KEY:
    raise RuntimeError("CRITICAL: SECRET_KEY environment variable is not set.")
