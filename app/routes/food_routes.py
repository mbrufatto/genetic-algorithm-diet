from flask import Blueprint, jsonify
from ..models.food import Food

food_bp = Blueprint('food', __name__)

@food_bp.route("/api/food", methods=["GET"])
def get_foods():
    foods = Food.query.all
    return jsonify([food.to_dict() for food in foods])
