import os


class Config:
    DEBUG = False
    DEVELOPMENT = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", "find-me-if-you-can")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql:///flask_diary")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    pass


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"  # in-memory test database


class ProductionConfig(Config):
    DEBUG = False


configs = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig
}
