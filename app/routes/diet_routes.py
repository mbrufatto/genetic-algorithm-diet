from flask import Blueprint, jsonify, request

from ..models.dieta_command import DietaCommand
from ..services.genetic import generate_diet, generate_diet_on_command
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


@diet_bp.route("/post-diet", methods=["POST"])
def post_diet():
    data = request.get_json()
    command = DietaCommand(
        porcoes=data.get("porcoes"),
        calorias=data.get("calorias"),
        proteinas=data.get("proteinas"),
        lipidios=data.get("lipidios"),
        carboidratos=data.get("carboidratos"),
        fibras=data.get("fibras"),
        categorias=data.get("categorias"),
    )
    db_session = next(get_db())
    return generate_diet_on_command(db_session, command)

