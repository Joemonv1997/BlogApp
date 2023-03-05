from blog.home import home_blueprint
from blog.auth import auth_blueprint


def blog_main(app):
    app.register_blueprint(home_blueprint, url_prefix="/")
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
