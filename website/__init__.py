from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = '75ca7f94106b75b9'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    db.init_app(app)

    from website.views import views

    app.register_blueprint(views)

    create_database(app)

    from .models import City

    return app


def create_database(app):
    if not path.exists('website/' + 'site.db'):
        db.create_all(app=app)
        print('Database created!')
