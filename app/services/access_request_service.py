from app.core.exceptions import NotFoundError
from app.extensions import db
from app.models.access_request import AccessRequest
from app.repositories.access_request_repository import AccessRequestRepository
from app.repositories.data_product_repository import DataProductRepository


class AccessRequestService:
    @staticmethod
    def create(data, current_user):
        data_product = DataProductRepository.get_by_id_and_organization(
            data["data_product_id"], current_user.organization_id
        )
        if data_product is None or not data_product.is_active:
            raise NotFoundError("Data product not found")

        access_request = AccessRequest(
            organization_id=current_user.organization_id,
            requester_id=current_user.id,
            data_product_id=data_product.id,
            access_level=data["access_level"],
            business_justification=data["business_justification"].strip(),
            expiration_date=data["expiration_date"],
        )

        AccessRequestRepository.add(access_request)
        db.session.commit()

        return access_request

    @staticmethod
    def list_for_user(current_user):
        return AccessRequestRepository.list_for_requester(
            current_user.organization_id, current_user.id
        )

    @staticmethod
    def get_for_user(access_request_id, current_user):
        access_request = AccessRequestRepository.get_by_id_for_requester(
            access_request_id,
            current_user.organization_id,
            current_user.id,
        )

        if access_request is None:
            raise NotFoundError("Access request not found")

        return access_request
