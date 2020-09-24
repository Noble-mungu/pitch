import os

class Config:

   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:azbycx567@localhost/pitchperfect'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY ='WOOWEDNESDAY'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):

    '''
    ProdConfig
    '''
    DEBUG = True

class DevConfig(Config):
    pass
    

config_options = {
'development':DevConfig,
'production':ProdConfig
}