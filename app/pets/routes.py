from flask import request, render_template, redirect, flash
from app.pets import bp
from app.services.pet_service import PetService
from app.utils.alert_type import AlertType
from app.utils.flash_message import FlashMessage
from app.utils.helpers import login_required

@bp.route('/')
def index():
    return render_template(
        "pets/index.html", 
        options=PetService.get_options(request), 
        pagination_result=PetService.get_pets(request)
        )

@bp.route('register', methods=["GET", "POST"])
@login_required
def register():
    if request.method == 'POST':
        register = PetService.register_pet(request)
        if not register:
            return redirect("/users/login")
        flash(FlashMessage("Pet added!", AlertType.SUCCESS.value ))
    types = PetService.get_pets_kind()
    return render_template("pets/register.html", types=types)