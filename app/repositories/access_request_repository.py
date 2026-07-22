from app.extensions import db
from app.models.access_request import AccessRequest


class AccessRequestRepository:

    @staticmethod
    def add(access_request):
        db.session.add(access_request)

    @staticmethod
    def get_by_id_for_requester(access_request_id, organization_id, requester_id):
        statement = db.select(AccessRequest).where(
            AccessRequest.id == access_request_id,
            AccessRequest.organization_id == organization_id,
            AccessRequest.requester_id == requester_id,
        )
        return db.session.scalar(statement)

    @staticmethod
    def list_for_requester(organization_id, requester_id):
        statement = (
            db.select(AccessRequest)
            .where(
                AccessRequest.organization_id == organization_id,
                AccessRequest.requester_id == requester_id,
            )
            .order_by(AccessRequest.created_at.desc(), AccessRequest.id.desc())
        )

        return db.session.scalars(statement).all()
