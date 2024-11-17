from werkzeug.datastructures import ImmutableMultiDict
from flask import flash
from app.models.user import User
from app.extensions import db
from app.utils.alert_type import AlertType
from app.utils.errors.users.user_register_errors import UserRegisterErrors
from app.utils.flash_message import FlashMessage
from app.utils.validators import UserValidators
class UserService:
  
  @staticmethod
  def register_user(form: ImmutableMultiDict):
    try:
      name: str = UserValidators.is_valid_user_name(form.get("name"))
      lastname: str = UserValidators.is_valid_user_name(form.get("lastname"),True)
      birth_date = UserValidators.is_valid_birth_date(form.get("birthdate"))
      phone_number: str = UserValidators.is_valid_phone_number(form.get("phonenumber"))
      email: str = UserValidators.is_valid_email(form.get("email"))
      password: str = form.get("password")
      password_confirmation: str = form.get("password_confirmation")
      address: str = UserValidators.is_valid_address(form.get("address"))
      
      new_user = User(
        username="test", 
        name=name, 
        lastname=lastname, 
        email=email, 
        password=UserValidators.passwords_match(password, password_confirmation),
        birth_date= birth_date,
        address=address,
        phone_number=phone_number
      )

      db.session.add(new_user)
      db.session.commit()
      db.session.flush()
    except UserRegisterErrors as e:
      flash(FlashMessage(e.message, AlertType.DANGER.value ))
      db.session.rollback()