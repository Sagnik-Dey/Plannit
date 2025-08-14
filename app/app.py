from flask import Flask
from dotenv import load_dotenv
import sys
import os

sys.path.append("app")
from landing import landing_bp
from login import login_bp
from home import home_bp
from update import update_bp
from view import view_bp
from delete import delete_bp
from register import register_bp
from logout import logout_bp

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get('SECRET_KEY')
    app.register_blueprint(landing_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(update_bp)
    app.register_blueprint(view_bp)
    app.register_blueprint(delete_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(logout_bp)
    
    return app