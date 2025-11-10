import os
from app import create_app
from app.models import db

config_name = os.getenv('FLASK_ENV', 'development')
app = create_app(config_name)

with app.app_context():
    pass

if __name__ == '__main__':
    print("=" * 60)
    print(" Starting Word Puzzle Game API")
    print("=" * 60)
    print(f" Environment: {config_name}")

    db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    if '@' in db_uri:
        db_display = db_uri.split('@')[1]
    else:
        db_display = 'Not configured'
    print(f" Database: {db_display}")

    print(f"Server: http://localhost:5000")
    print(f"Debug Mode: {app.config['DEBUG']}")
    print("=" * 60)
    print("\n Press CTRL+C to stop the server\n")

    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=5000)
