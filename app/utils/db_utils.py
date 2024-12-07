from app.extensions import db
from app.models.user import User
from app.models.pet import Pet
from app.models.pet_kind import PetKind
from app.models.adoptions import Adoptions
from app.models.adoption_status import AdoptionStatus
from datetime import date
from random import randrange
from werkzeug.security import generate_password_hash

class DBUtils():
  def setup_db(app):
    if not app:
      Exception("this function needs app context to be ran, please provide app")
    with app.app_context():
      db.create_all()
      
      """User"""
      new_user = User(
        name="Xavi", 
        lastname="Alonso", 
        email="x@d.co", 
        password=generate_password_hash("123456"),
        birth_date= date(1990,12,30),
        address="1234 Main St",
        phone_number="1123873991"
      )
      db.session.add(new_user)
      db.session.commit()

      """Pet kinds"""
      dog = PetKind(name="Dog")
      cat = PetKind(name="Cat")
      db.session.add_all([dog,cat])
      db.session.commit()
      
      """Pets"""
      pets = []
      for i in range(40):
        kind_id=randrange(1,3,1)
        pets.append(Pet(
          name=f"Pet {str(i)}", 
          kind_id=kind_id,
          age=randrange(0,8),
          img_src="img/placeholder-dog.jpg" if kind_id == 1 else "img/placeholder-cat.jpg",
          weight=1,
          location="Shelbyville", 
          sex= "M" if randrange(3) > 1.5 else "F",
          height=1,
          registrar_id=1
          ))
      db.session.add_all(pets)
      db.session.commit()
      db.session.flush()
      
  def drop_db(app):
    with app.app_context():
      db.drop_all()

