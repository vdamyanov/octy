class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/octy_dev'
    SENDGRID_USER = 'octy'
    SENDGRID_KEY = 'mrKimJongSexyGloriousBeast7'

class Prod(Config):
    DEBUG = False

class Stage(Config):
    DEVELOPMENT = True
    DEBUG = True

class Dev(Config):
    DEVELOPMENT = True
    DEBUG = True

class Test(Config):
    TESTING = True
