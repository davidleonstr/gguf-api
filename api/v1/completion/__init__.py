from flask import Blueprint

completionbp = Blueprint('completion', __name__)

# Load routes
from . import routes
__load__ = [routes]

__all__ = ['completionbp']