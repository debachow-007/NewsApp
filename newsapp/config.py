import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    NEWS_API_KEY = os.getenv('NEWS_API_KEY')
    