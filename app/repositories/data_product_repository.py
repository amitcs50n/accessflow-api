from app.extensions import db
from app.models.data_product import DataProduct


class DataProductRepository:
    @staticmethod
    def add(data_product):
        db.session.add(data_product)

    @staticmethod
    def get_by_id_and_organization(data_product_id, organization_id):
        statement = db.select(DataProduct).where(
            DataProduct.id == data_product_id,
            DataProduct.organization_id == organization_id,
        )
        return db.session.scalar(statement)

    @staticmethod
    def list_by_organization(organization_id):
        statement = (
            db.select(DataProduct)
            .where(DataProduct.organization_id == organization_id)
            .order_by(DataProduct.id)
        )

        return db.session.scalar(statement)
