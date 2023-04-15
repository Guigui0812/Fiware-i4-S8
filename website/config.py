import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

# Enable debug mode, that will refresh the page when you make changes.
DEBUG = True
SESSION_TYPE = 'filesystem'

basedir = os.path.abspath(os.path.dirname(__file__))