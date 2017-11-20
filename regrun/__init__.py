import os

from flask import Flask
from flask_socketio import SocketIO

from assets import assets
from forms import ScheduleTestForm
from flask_mongoalchemy import MongoAlchemy
from config import config

basedir = os.path.dirname(os.path.abspath(__file__))

# Flask extensions
db = MongoAlchemy()
socketio = SocketIO()

# Import Socket.IO events so that they are registered with Flask-SocketIO
from . import events

# Import models so that they are registered with MongoAlchemy
from . import models


def create_app(config_name=None):
    """Entry point to flask-script"""
    app = Flask(__name__)
    app.clients = {}
    if config_name is None:
        config_name = os.environ['REGRUN_CONFIG']
    app.config.from_object(config[config_name]())

    # Initialize app extensions
    db.init_app(app)
    assets.init_app(app)
    socketio.init_app(app)

    from regrun import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
