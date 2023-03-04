from flask import Flask
from flask_cors import CORS
from blog import blog_main
def manageApp():
    app=Flask(__name__)
    blog_main(app)
    CORS(app,origin="*")
    return app