from flask import Blueprint

bp = Blueprint('us', __name__)
from app.us import routes