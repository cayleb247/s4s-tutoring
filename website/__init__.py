from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'a507cf82d9cd01dcc897937bf985231c32eca78bd16efae7597519ddf982da57'

    from .views import views

    app.register_blueprint(views, url_prefix='/')
    
    return app