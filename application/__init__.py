from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__) # Initialize the Flask application
app.config.from_object(Config)  # Load configuration from the Config class

db = SQLAlchemy(app)  # Initialize the SQLAlchemy database instance
migrate = Migrate(app, db)  # Initialize the Flask-Migrate instance
login = LoginManager(app)  # Initialize the Flask-Login instance
login.login_view = 'login'  # Set the login view for Flask-Login
from application import routes, models  # Import the routes module to register the routes
