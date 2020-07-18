import os

base_dir = os.getcwd()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_URI') or 'sqlite:///' + os.path.join(base_dir, 'your_db_name')

class TestsConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TESTS_URI') or 'sqlite:///' + os.path.join(base_dir, 'test_db_name')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')


config = {
    'development': DevelopmentConfig,
    'testing': TestsConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}