from datetime import datetime
from sqlalchemy.orm import mapped_column
from app.extensions import db

class User(db.Model):
  id = mapped_column(db.Integer, primary_key=True, autoincrement=True)
  username = mapped_column(db.String(255), nullable=False)
  email = mapped_column(db.String(255), nullable=False)
  password = mapped_column(db.String(255), nullable=False)
  name = mapped_column(db.String(255), nullable=False)
  lastname = mapped_column(db.String(255), nullable=False)
  birth_date = mapped_column(db.Date, nullable=False)
  address = mapped_column(db.String(255), nullable=False)
  phone_number = mapped_column(db.String(255), nullable=False)
  registration_date = mapped_column(db.DateTime, default=datetime.utcnow, nullable=False)