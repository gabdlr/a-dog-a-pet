from flask import redirect, request, render_template, session
from app.services.user_service import UserService
from app.users import bp
from app.utils.form_errors_dict import FORM_ERRORS
from app.utils.helpers import login_required

@bp.route('/', methods=["GET", "POST"])
@login_required
def index():
    user = UserService.get_user()
    if user is None:
        return redirect("login")
    user = user[0]
    if request.method == 'POST':
        if request.form.get("password_update"):
            UserService.update_password(request.form, user)
        elif request.form.get("personal_information"):
            UserService.update_personal_info(request.form, user)
    return render_template("users/index.html",user=user,FORM_ERRORS=FORM_ERRORS)

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
