from sqlalchemy import func

from app.core.constants import AccessRequestStatus, SourceSystem
from app.extensions import db


class AccessRequest(db.Model):
    __tablename__ = "access_requests"

    id = db.Column(db.Integer, primary_key=True)

    organization_id = db.Column(
        db.Integer, db.ForeignKey("organizations.id"), nullable=False
    )
    requester_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    data_product_id = db.Column(
        db.Integer, db.ForeignKey("data_products.id"), nullable=False
    )
    access_level = db.Column(db.String(50), nullable=False)
    business_justification = db.Column(db.Text, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)
    status = db.Column(
        db.String(50),
        nullable=False,
        default=AccessRequestStatus.DRAFT.value,
        server_default=AccessRequestStatus.DRAFT.value,
    )
    source_system = db.Column(
        db.String(50),
        nullable=False,
        default=SourceSystem.INTERNAL.value,
        server_default=SourceSystem.INTERNAL.value,
    )
    servicenow_request_number = db.Column(db.String(100), nullable=True)
    servicenow_sys_id = db.Column(db.String(100), nullable=True)
    created_at = db.Column(
        db.DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    organization = db.relationship(
        "Organization",
        back_populates="access_requests",
    )
    requester = db.relationship(
        "User",
        back_populates="submitted_access_requests",
        foreign_keys=[requester_id],
    )
    data_product = db.relationship(
        "DataProduct",
        back_populates="access_requests",
    )
