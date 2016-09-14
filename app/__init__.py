from flask import Flask, render_template
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.pymongo import PyMongo
from config import config


mail = Mail()
moment = Moment()
db = PyMongo()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    
    
    # TODO (09/14/2016 Night) @thislight: Add blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)
    
    
    return app




