from app.extensions import db
from app.models.user import User
from app.models.pet import Pet
from app.models.pet_kind import PetKind
from app.models.adoptions import Adoptions
from app.models.adoption_status import AdoptionStatus

class DBUtils():
  def setup_db(app):
    if not app:
      Exception("this function needs app context to be ran, please provide app")
    with app.app_context():
      db.create_all()

  def drop_db(app):
    with app.app_context():
      db.drop_all()

