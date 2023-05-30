import os

# Flask app configuration
SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'

# SQLite database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
