from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.security import generate_password_hash, check_password_hash

from flask import flash, session
from app.models.user import User
from app.extensions import db
from app.utils.alert_type import AlertType
from app.utils.errors.users.user_register_errors import UserRegisterErrors
from app.utils.flash_message import FlashMessage
from app.utils.validators import UserValidators
class UserService:
  
  @staticmethod
  def register_user(form: ImmutableMultiDict) -> bool :
    try:
      email: str = UserValidators.is_valid_email(form.get("email"))
      
      if db.session.execute(db.select(User).filter_by(email=email)).one_or_none() is not None:
        raise UserRegisterErrors("User email address is already taken")
      
      name: str = UserValidators.is_valid_user_name(form.get("name"))
      lastname: str = UserValidators.is_valid_user_name(form.get("lastname"),True)
      birth_date = UserValidators.is_valid_birth_date(form.get("birthdate"))
      phone_number: str = UserValidators.is_valid_phone_number(form.get("phonenumber"))
      password: str = form.get("password")
      password_confirmation: str = form.get("password_confirmation")
      address: str = UserValidators.is_valid_address(form.get("address"))
      
      new_user = User(
        username="test", 
        name=name, 
        lastname=lastname, 
        email=email, 
        password=generate_password_hash(UserValidators.passwords_match(password, password_confirmation)),
        birth_date= birth_date,
        address=address,
        phone_number=phone_number
      )

      db.session.add(new_user)
      db.session.commit()
      db.session.flush()
      user_row = db.session.execute(db.select(User).filter_by(email=email)).one_or_none()
      if user_row is not None:
        session["id"] = user_row[0].id
        return True
      raise UserRegisterErrors("Something went wrong")
    except UserRegisterErrors as e:
      flash(FlashMessage(e.message, AlertType.DANGER.value ))
      db.session.rollback()

  @staticmethod
  def login(form: ImmutableMultiDict):
        try:
          email = UserValidators.is_valid_email(form.get("email"))
          password = UserValidators.is_valid_password(form.get("password"))
          user_row = db.session.execute(db.select(User).filter_by(email=email)).one_or_none()
          if user_row is not None:
            if check_password_hash(user_row[0].password, password):
              session["id"] = user_row[0].id
              return True
          flash(FlashMessage("Invalid email or password", AlertType.DANGER.value ))
          return False
        except UserRegisterErrors as e:
          flash(FlashMessage(e.message, AlertType.DANGER.value ))

          