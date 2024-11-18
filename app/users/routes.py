from flask import redirect, request, render_template, session
from app.services.user_service import UserService
from app.users import bp
from app.utils.form_errors_dict import FORM_ERRORS
@bp.route('/')
def index():
    return render_template("users/index.html")

@bp.route('/login')
def login():
    return render_template("users/login.html")

@bp.route('/logout')
def logout():
    session.clear()
    return redirect("/")

@bp.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        if UserService.register_user(request.form):
            return redirect("/")
    return render_template("users/register.html", FORM_ERRORS=FORM_ERRORS)
