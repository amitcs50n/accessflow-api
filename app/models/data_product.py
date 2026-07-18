from sqlalchemy import func

from app.extensions import db


class DataProduct(db.Model):
    __tablename__ = "data_products"

    id = db.Column(db.Integer, primary_key=True)

    organization_id = db.Column(
        db.Integer, db.ForeignKey("organizations.id"), nullable=False
    )

    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    platform = db.Column(db.String(50), nullable=False)
    sensitivity_level = db.Column(db.String(50), nullable=False)

    owner_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    target_role_or_group = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    created_at = db.Column(
        db.DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    updated_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    organization = db.relationship("Organization", back_populates="data_products")

    owner = db.relationship(
        "User", back_populates="owned_data_products", foreign_keys=[owner_user_id]
    )
