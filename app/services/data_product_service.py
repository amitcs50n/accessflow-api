from app.core.exceptions import NotFoundError
from app.extensions import db
from app.models.data_product import DataProduct
from app.repositories.data_product_repository import DataProductRepository
from app.repositories.user_repository import UserRepository


class DataProductService:
    @staticmethod
    def _validate_owner(owner_user_id, organization_id):
        owner = UserRepository.get_by_id(owner_user_id)

        if owner is None or owner.organization_id != organization_id:
            raise NotFoundError("Owner user not found")

        return owner

    @staticmethod
    def create(data, current_user):
        owner = DataProductService._validate_owner(
            data["owner_user_id"], current_user.organization_id
        )

        data_product = DataProduct(
            organization_id=current_user.organization_id,
            name=data["name"].strip(),
            description=data["description"].strip(),
            platform=data["platform"],
            sensitivity_level=data["sensitivity_level"],
            owner_user_id=owner.id,
            target_role_or_group=data["target_role_or_group"].strip(),
        )
        DataProductRepository.add(data_product)
        db.session.commit()

        return data_product

    @staticmethod
    def list_for_user(current_user):
        return DataProductRepository.list_by_organization(current_user.organization_id)

    @staticmethod
    def get_for_user(data_product_id, current_user):
        data_product = DataProductRepository.get_by_id_and_organization(
            data_product_id, current_user.organization_id
        )

        if data_product is None:
            raise NotFoundError("Data product not found")

        return data_product

    @staticmethod
    def update(data_product_id, data, current_user):
        data_product = DataProductService.get_for_user(
            data_product_id,
            current_user,
        )

        if "owner_user_id" in data:
            owner = DataProductService._validate_owner(
                data["owner_user_id"],
                current_user.organization_id,
            )
            data["owner_user_id"] = owner.id

        text_fields = {
            "name",
            "description",
            "target_role_or_group",
        }

        for field, value in data.items():
            if field in text_fields:
                value = value.strip()

            setattr(data_product, field, value)
            # setattr() is a built-in Python function used to set (or update) an attribute of an object dynamically.

        db.session.commit()

        return data_product
