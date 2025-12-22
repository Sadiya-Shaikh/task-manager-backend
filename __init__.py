import os
from flask import Flask
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

from app.health.routes import main_bp
from app.auth.routes import auth_bp
from app.tasks.routes import tasks_bp
from app.models import db

def create_app():
    load_dotenv()

    app = Flask(__name__)

    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "dev-secret")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    JWTManager(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app
