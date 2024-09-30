from flask import Blueprint, jsonify, request

from ..models.diet_command import DietaCommand
from ..models.diet_config import DietaConfig
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


@diet_bp.route("/diet/create", methods=["POST"])
def post_diet():
    data = request.get_json()
    command = DietaCommand(
        porcoes=int(data.get("meta").get("porcoes", 5)),
        calorias=int(data.get("meta").get("calorias", 700)),
        proteinas=int(data.get("meta").get("proteinas", 15)),
        lipidios=int(data.get("meta").get("lipidios", 14)),
        carboidratos=int(data.get("meta").get("carboidratos", 75)),
        fibras=int(data.get("meta").get("fibras", 8)),
        categorias=data.get("meta").get("categorias", ["Cereais", "Frutas", "Pescados"]) if data.get("meta").get("categorias") is not None else [],
    )
    config = DietaConfig(
        tamanho_populacao=data.get("config").get("tamanho_populacao", 0),
        maximo_evolucoes=int(data.get("config").get("maximo_evolucoes", 0)),
        elite_proporcao=float(data.get("config").get("elite_proporcao", 0.0)),
        mutacao_proporcao=float(data.get("config").get("mutacao_proporcao", 0.0)),
    )
    db_session = next(get_db())
    return generate_diet_on_command(db_session, config, command)

