from flask import Flask
from flask_cors import CORS
from .config import DATABASE_URI
from .database import db
from .populate_db import populate_db
from .routes.diet_routes import diet_bp
from .routes.food_routes import food_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configuração do SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Criar o banco de dados e popular
    with app.app_context():
        db.create_all()
        populate_db()

    # Registrar os blueprints
    app.register_blueprint(diet_bp)
    app.register_blueprint(food_bp)

    return app