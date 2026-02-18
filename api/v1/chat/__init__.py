from flask import Blueprint

chatbp = Blueprint('chat', __name__)

# Load routes
from . import routes
__load__ = [routes]

__all__ = ['chatbp']