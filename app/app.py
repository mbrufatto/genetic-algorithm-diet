# from flask import Flask, jsonify
# from flask_cors import CORS
# from db import db
# from app.populate_db import populate_db

# from app.services.genetic import generate_diet

# app = Flask(__name__)
# CORS(app)

# # Configuração do SQLite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db.init_app(app)

# # Importar os modelos
# # from app.models.food import Food

# # Criar o banco de dados
# with app.app_context():
#     db.create_all()
#     populate_db()

# @app.route("/")
# def helloWorld():
#     return "Hello, cross-origin-world!"


# # sanity check route
# @app.route("/ping", methods=["GET"])
# def ping_pong():
#     return jsonify("porong!")


# @app.route("/get-diet", methods=["GET"])
# def get_diet():
#     return generate_diet()

# # Rota para obter todos os alimentos
# @app.route("/api/products", methods=["GET"])
# def get_products():
#     products = Food.query.all()
#     return jsonify([product.to_dict() for product in products])

# if __name__ == "__main__":
#     app.run()
