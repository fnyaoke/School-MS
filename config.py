import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')



    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://student:Amazeing16@localhost/school_ms'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
#    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass
class TestConfig(Config):
#    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://student:Amazeing16@localhost/one_min_app_test'
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
#    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://student:Amazeing16@localhost/one_min_app'
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}

