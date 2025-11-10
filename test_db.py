from app import create_app

from app.models import db

app = create_app('development')

with app.app_context():
    try:

        # Test connection

        db.session.execute('SELECT 1')

        print(" Database connection successful!")

    except Exception as e:

        print(f" Database connection failed: {e}")
