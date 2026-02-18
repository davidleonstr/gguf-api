from flask import Blueprint
from api.v1.chat import chatbp

v1bp = Blueprint('v1', __name__)

# Register v1 blueprints
v1bp.register_blueprint(chatbp, url_prefix='/chat')