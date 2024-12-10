from app.extensions import db
from sqlalchemy.orm import relationship, mapped_column

class Adoptions(db.Model) :
  id = mapped_column(db.Integer, primary_key=True)
  adopter_id = mapped_column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  pet_id = mapped_column(db.Integer, db.ForeignKey('pet.id'), nullable=False)
  status_id = mapped_column(db.Integer, db.ForeignKey('adoption_status.id'), nullable=False)
  adopter = relationship("User")
  status = relationship("AdoptionStatus", uselist=False)