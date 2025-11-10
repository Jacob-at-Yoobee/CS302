from flask import Flask
from flask_migrate import Migrate
from app.models import db
from app.config import config

migrate = Migrate()


def create_app(config_name='default'):
    app = Flask(__name__, template_folder='../templates')

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    @app.shell_context_processor
    def make_shell_context():
        from app.models import Player, Word
        return {'db': db, 'Player': Player, 'Word': Word}

    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Resource not found'}, 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return {'error': 'Internal server error'}, 500

    return app
