import os
import sys
from flask import Flask
from flask_cors import CORS
from blog import blog_main

sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "repository"
    )
)
from models import Base, Session, engine


def manageApp():
    app = Flask(__name__)
    Base.metadata.create_all(bind=engine)
    blog_main(app)
    CORS(app, origin="*")
    return app
