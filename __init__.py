from flask import Flask
from app.health.routes import health_bp
from app.auth.routes import auth_bp

def create_app():
    app = Flask(__name__)
    
    # Register Blueprints
    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp)
    
    return app