class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '11dac81d112effeb1c8c7a83f7a5175d'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True