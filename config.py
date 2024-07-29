import os

class Config(object):
    API_TITLE   =   "Flask API"
    API_VERSION =   "1.0.0"
    
    DEBUG   =   True
    TESTING =   False
    TEMPLATES_AUTO_RELOAD   =   True
    PERMANENT_SESSION_LIFETIME  =   3600
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS    =   True
    
    JWT_SECRET_KEY  =   os.environ.get('SECRET_KEY')
    CRSF_ENABLED    =   True
    
    OPENAPI_VERSION =   "3.0.3"
    OPENAPI_URL_PREFIX  =   "/"
    OPENAPI_SWAGGER_UI_PATH =   "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL  =   "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    
class ProductionConfig(Config):
	DEBUG = False

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True
