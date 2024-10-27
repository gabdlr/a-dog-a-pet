from app.extensions import db

class AdoptionStatus(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  status = db.Column(db.String(255), nullable=False)