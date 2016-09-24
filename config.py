import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hereacg_webapp'
    HEREACG_MAIL_SUBJECT_PREFIX = '[HereACG]'
    HEREACG_MAIL_SENDER = 'HereACG NoReply <noreply@hereacg.com>'
    HEREACG_ADMIN = os.environ.get('HEREACG_ADMIN')
    
    
    @staticmethod
    def init_app(app):
        pass
    
    

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'stmp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MONGO_URI = os.environ.get('DEV_DB_URI') or 'mongodb://localhost:27017'
    

class TestingConfig(Config):
    TESTING =True
    MONGO_URI = os.environ.get('TEST_DB_URI') or 'mongodb://localhost:27017'


class ProductionConfig(Config):
    MONGO_URI = os.environ.get('DB_URI') or 'mongodb://localhost:27017'
    

config = {
    'devlopment': DevlopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    
    'default': DevlopmentConfig
    }





