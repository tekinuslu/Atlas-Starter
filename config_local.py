import os

import ipdb

ipdb.set_trace()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    # app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    SECRET_KEY = "'{}'".format(os.urandom(24))
    PORT = 5500
    # SERVER_NAME = 'localhost.localdomain' + ':' + str(PORT)
    HOST = "http://localhost" + ":" + str(PORT)

    ##################################
    ## Database SETTINGS
    #################################
    ## SQlite
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI_sqlite = "sqlite:///" + os.path.join(basedir, "db.sqlite")
    #
    SQLALCHEMY_DATABASE_URI = (
        SQLALCHEMY_DATABASE_URI_sqlite  # kept for manage.py init db
    )

    SQLALCHEMY_BINDS = {"db1": SQLALCHEMY_DATABASE_URI_sqlite}


class ProductionConfig(Config):
    DEBUG = False
    # SECRET_KEY = 'this-really-needs-to-be-changed'
    SECRET_KEY = "9OLWxND4o83j4K4iuopO"


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    PORT = 5700
    HOST = "http://localhost" + ":" + str(PORT)


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    DEBUG = True
    PORT = 5700
    HOST = "http://localhost" + ":" + str(PORT)
    JSON_SORT_KEYS = False  # testing, disabled for visualisation purpose
    # https://github.com/marshmallow-code/marshmallow/issues/257


class TestingConfig(Config):
    ENV = "testing"
    TESTING = True
