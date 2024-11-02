from flask import render_template
from app.users import bp

@bp.route('/')
def index():
    return render_template("users/index.html")

@bp.route('/login')
def login():
    return render_template("users/login.html")

@bp.route('/register')
def register():
    return render_template("users/register.html")
