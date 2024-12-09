from functools import wraps
from flask import redirect, session

def login_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("id") is None:
            return redirect("/users/login")
        return f(*args, **kwargs)

    return decorated_function

def only_guests(html: str):
    if not session["id"]:
       return html
    return None

def pet_sex_id_to_str(sex: str):
    if sex == '1':
        return 'F'
    elif sex == '2':
        return 'M'
    else:
        return None