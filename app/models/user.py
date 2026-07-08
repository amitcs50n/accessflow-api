from sqlalchemy import func
from app.extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    roll_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    roll = db.relationship("Role", back_populates=True)
    access_request = db.relationship("AccessRequest", back_populates="requester")
