import os

class Config(object):
    DEBUG = True
    DEVELOPMENT = True

class Development(Config):
    DEBUG = True
    DEVELOPMENT = True  

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False