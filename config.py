import os

class Config:

   
    SQLALCHEMY_DATABASE_URI = 'postgres://odvwihklcvlsfx:0b63486d69f81a4b35556aee4cbd8f707dc1dfb7f35eeec2a0483d7d5d51d80b@ec2-3-224-97-209.compute-1.amazonaws.com:5432/d1ip0kuc1sm40h'
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