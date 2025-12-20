from flask import Flask
from flask_jwt_extended import JWTManager
from app.models import db
from app.health.routes import main_bp
from app.auth.routes import auth_bp
import os

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
    app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")

    db.init_app(app)
    JWTManager(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()

    return app