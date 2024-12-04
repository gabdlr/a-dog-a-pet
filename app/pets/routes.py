from flask import request, render_template
from app.pets import bp
from app.services.pet_service import PetService

@bp.route('/')
def index():
    return render_template("pets/index.html", options=PetService.get_options(request))