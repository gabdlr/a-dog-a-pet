from flask import flash, render_template, request, session
from app.us import bp
from app.extensions import db
from app.models.user import User
from app.utils.alert_type import AlertType
from app.utils.flash_message import FlashMessage

@bp.route('contact', methods=['GET', 'POST'])
def contact():
    user = None
    user_id = session.get('id')
    if request.method == 'POST':
        flash(FlashMessage("Message sent! (not really :$)", AlertType.SUCCESS.value))
    
    if user_id is not None:
        user = db.session.execute(db.select(User).filter_by(id=user_id)).one_or_none()
        if user is not None:
            user = user[0]
    return render_template("us/contact.html",user=user)

@bp.route('about')
def about():
    return render_template("us/about.html")