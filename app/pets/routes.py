from flask import request, render_template
from app.pets import bp
from app.services.pet_service import PetService
from app.utils.helpers import login_required

@bp.route('/')
def index():
    return render_template(
        "pets/index.html", 
        options=PetService.get_options(request), 
        pagination_result=PetService.get_pets(request)
        )

@bp.route('register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        PetService.register_pet(request)
    types = PetService.get_pets_kind()
    return render_template("pets/register.html", types=types)