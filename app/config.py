import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '..', '.env'))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-this')

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
                              f"postgresql://{os.getenv('DB_USER', 'postgres')}:" \
                              f"{os.getenv('DB_PASSWORD', '')}@" \
                              f"{os.getenv('DB_HOST', 'localhost')}:" \
                              f"{os.getenv('DB_PORT', '5432')}/" \
                              f"{os.getenv('DB_NAME', 'word_puzzle_db')}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = os.getenv('SQLALCHEMY_ECHO', 'True').lower() == 'true'
    JSON_SORT_KEYS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True

    @staticmethod
    def init_app(app):
        Config.init_app(app)
        print("🔧 Development mode enabled")


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SECRET_KEY = os.getenv('SECRET_KEY')

    @staticmethod
    def init_app(app):
        Config.init_app(app)
        if not app.config['SECRET_KEY']:
            raise ValueError("SECRET_KEY must be set in production")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
