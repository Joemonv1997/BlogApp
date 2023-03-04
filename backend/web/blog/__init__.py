from blog.home import home_blueprint

def blog_main(app):
    app.register_blueprint(home_blueprint,url_prefix="/")