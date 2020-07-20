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
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_URI') or 'sqlite:///' + os.path.join(base_dir, 'smapp_dev.sqlite')

class TestsConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TESTS_URI') or 'sqlite:///' + os.path.join(base_dir, 'smapp_test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://vevrkoatacowzo:60f7c7aae924a31ed6c60a7b1203ad64371a19816a91199c853f751b9c847c3a@ec2-50-16-198-4.compute-1.amazonaws.com:5432/d208ssdfa19i2f'


config = {
    'development': DevelopmentConfig,
    'testing': TestsConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
