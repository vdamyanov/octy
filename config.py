class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SENDGRID_USER = 'octy'
    SENDGRID_KEY = 'mrKimJongSexyGloriousBeast7'
    LINKEDIN_KEY='tgqpmdbwrca8',
    LINKEDIN_SECRET='udCHlYrbPLbLVNH1'

class Prod(Config):
    DEBUG = False

class Stage(Config):
    DEVELOPMENT = True
    DEBUG = True

class Dev(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/octy_dev'
    DEVELOPMENT = True
    DEBUG = True

class Test(Config):
    TESTING = True
