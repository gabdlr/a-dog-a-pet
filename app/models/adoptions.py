from app.extensions import db
import datetime
from sqlalchemy.orm import relationship, mapped_column

class Adoptions(db.Model) :
  id = mapped_column(db.Integer, primary_key=True)
  publisher_id = mapped_column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  pet_id = mapped_column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
  publish_date = mapped_column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
  status_id = mapped_column(db.Integer, db.ForeignKey('adoption_status.id'), nullable=False)
  publisher = relationship("User")
  pet = relationship("Pet")
  status = relationship("AdoptionStatus")