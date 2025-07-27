from flask import Flask
from config import Config

app = Flask(__name__) # Initialize the Flask application
app.config.from_object(Config)  # Load configuration from the Config class

from application import routes  # Import the routes module to register the routes
