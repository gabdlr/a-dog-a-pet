from flask import Blueprint

bp = Blueprint('pets', __name__)
from app.pets import routes