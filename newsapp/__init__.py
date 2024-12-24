from flask import Flask
from newsapp.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    from newsapp.main.routes import main
    app.register_blueprint(main)
    
    return app