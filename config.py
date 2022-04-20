import os

from dotenv import load_dotenv

sqlite_uri = os.path.abspath("app/database/database.db")
project_root = os.getcwd()
load_dotenv(os.path.join(project_root, '.env'))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI") or "sqlite:///" + sqlite_uri
