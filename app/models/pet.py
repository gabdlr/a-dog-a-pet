import datetime
from sqlalchemy.orm import relationship, mapped_column
from app.extensions import db

class Pet(db.Model):
  id = mapped_column(db.Integer, primary_key=True)
  name = mapped_column(db.String(255), nullable=False)
  kind_id = mapped_column(db.Integer, db.ForeignKey('pet_kind.id'), nullable=False)
  age = mapped_column(db.Integer, default=0, nullable=False)
  weight = mapped_column(db.Float, default=0, nullable=False)
  location = mapped_column(db.String(255), nullable=False)
  sex = mapped_column(db.String(1), nullable=False)
  height = mapped_column(db.Float, default=0, nullable=False)
  registrar_id = mapped_column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  registration_date = mapped_column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
  kind = relationship("PetKind")
  registrar = relationship("User")