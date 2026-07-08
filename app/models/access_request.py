from sqlalchemy import func

from app.extensions import db


class AccessRequest(db.Model):
    __tablename__ = "access_requests"

    id = db.Column(db.Integer, primary_key=True)
    requester_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    system_name = db.Column(db.String(100), nullable=False)
    access_level = db.Column(db.String(100), nullable=False)
    justification = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(30), nullable=False, default="pending")
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    requester = db.relationship("User", back_populates="access_requests")
