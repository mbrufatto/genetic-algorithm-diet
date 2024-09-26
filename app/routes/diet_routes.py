from flask import Blueprint, jsonify
from sqlalchemy.orm import Session
from ..services.genetic import generate_diet
from ..database import get_db

diet_bp = Blueprint('diet', __name__)

@diet_bp.route("/get-diet", methods=["GET"])
def get_diet():
    db_session = next(get_db())
    return generate_diet(db_session)

@diet_bp.route("/get-diet-json", methods=["GET"])
def get_diet_json():
    db_session = next(get_db())
    dieta = generate_diet(db_session)
    return jsonify(dieta)