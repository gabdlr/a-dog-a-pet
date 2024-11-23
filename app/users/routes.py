from flask import redirect, request, render_template, session
from app.services.user_service import UserService
from app.users import bp
from app.utils.form_errors_dict import FORM_ERRORS
from app.utils.helpers import login_required

@bp.route('/')
@login_required
def index():
    return render_template("users/index.html")

@bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        if UserService.login(request.form):
           return redirect("/users/")
    return render_template("users/login.html", FORM_ERRORS=FORM_ERRORS)

@bp.route('/logout')
def logout():
    session.clear()
    return redirect("/")

@bp.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        if UserService.register_user(request.form):
            return redirect("/users/")
    return render_template("users/register.html", FORM_ERRORS=FORM_ERRORS)
