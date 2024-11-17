from datetime import date
from typing import Optional
from app.utils.errors.users.user_register_errors import UserRegisterErrors
import re
class UserValidators:
  
  @staticmethod
  def is_valid_user_name(name: Optional[str], isLastname=False):
    if(UserValidators.is_valid_str_and_pattern(name, '^[A-Za-z ]{2,255}$')):
        return name
    if(isLastname):
      raise UserRegisterErrors("Invalid user lastname")
    raise UserRegisterErrors("Invalid user name")
  
  @staticmethod
  def is_valid_birth_date(birth_date: Optional[str]):
    if(UserValidators.is_valid_str_and_pattern(birth_date, '^\d{4}-\d{2}-\d{2}$')):
      try:
        birth_date = [int(n) for n in (str(birth_date)).split("-")]
        return date(birth_date[0], birth_date[1], birth_date[2])
      except:
        raise UserRegisterErrors("Invalid user birthdate")
    raise UserRegisterErrors("Invalid user birthdate")

  @staticmethod
  def is_valid_phone_number(phone_number: Optional[str]):
    if(UserValidators.is_valid_str_and_pattern(phone_number, '^(\+\d{1,3}){0,1}[0-9]{7,255}$')):
      return phone_number
    raise UserRegisterErrors("Invalid user phone number")  

  @staticmethod
  def is_valid_email(email: Optional[str]):
    if(UserValidators.is_valid_str_and_pattern(email, '^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$')):
      if(len(email) <= 255):
        return email
    raise UserRegisterErrors("Invalid user email")
  
  @staticmethod
  def is_valid_address(address: Optional[str]):
    if(isinstance(address, str) and len(address) <= 255):
      return address
    raise UserRegisterErrors("Invalid user address")

  @staticmethod
  def is_valid_str_and_pattern(string: Optional[str], pattern: str):
    if(isinstance(string, str)):
      regex = re.compile(pattern)
      if(regex.match(string) is not None):
        return True
    return False
  
  @staticmethod
  def is_valid_password(password: str):
    if(isinstance(password, str)):
      password_len = len(password)
      if(password_len >= 6 and password_len <= 255):
        return password
    raise UserRegisterErrors("Invalid user password")
  
  @staticmethod
  def passwords_match(password: str, password_confirmation: str):
    if(UserValidators.is_valid_password(password) == UserValidators.is_valid_password(password_confirmation)):
      return password
    raise UserRegisterErrors("User password and password confirmation don't match")