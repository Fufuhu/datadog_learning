import os
from os.path import join, dirname
from dotenv import load_dotenv


# print(__file__)
dotenv_path = join(dirname(__file__), '.env')
# print(dotenv_path)
load_dotenv(dotenv_path)

API_KEY = os.environ.get("API_KEY")
APP_KEY = os.environ.get("APP_KEY")
