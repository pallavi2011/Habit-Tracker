import os
from flask import Flask
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv
import certifi

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.register_blueprint(pages)
    client = MongoClient(os.environ.get("MONGODB_URI"), tlsCAFile=certifi.where())
    app.db = client.get_default_database()

    return app