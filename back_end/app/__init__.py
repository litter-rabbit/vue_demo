from flask import Flask
from config import Baseconfig
from app.api.ping import api_bp
def create_app():

    app=Flask(__name__)
    app.config.from_object(Baseconfig)
    
    app.register_blueprint(api_bp,url_prefix='/api')
    return app





