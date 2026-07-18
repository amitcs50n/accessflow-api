from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from app.core.constants import UserRole
from app.core.permissions import require_roles
from app.core.security import get_current_user
from app.schemas.data_product import (
    DataProductCreateSchema,
    DataProductResponseSchema,
    DataProductUpdateSchema,
)
from app.services.data_product_service import DataProductService

data_products_bp = Blueprint(
    "data_products",
    __name__,
    url_prefix="/api/v1/data-products",
    description="Data product operations",
)


@data_products_bp.route("")
class DataProductListView(MethodView):
    @jwt_required()
    @data_products_bp.response(
        200,
        DataProductResponseSchema(many=True),
    )
    def get(self):
        current_user = get_current_user()
        return DataProductService.list_for_user(current_user)

    @jwt_required()
    @require_roles(
        UserRole.DATA_OWNER,
        UserRole.PLATFORM_ADMIN,
    )
    @data_products_bp.arguments(DataProductCreateSchema)
    @data_products_bp.response(201, DataProductResponseSchema)
    def post(self, data):
        current_user = get_current_user()
        return DataProductService.create(data, current_user)


# This is a separate top-level class.
@data_products_bp.route("/<int:data_product_id>")
class DataProductView(MethodView):
    @jwt_required()
    @data_products_bp.response(200, DataProductResponseSchema)
    def get(self, data_product_id):
        current_user = get_current_user()
        return DataProductService.get_for_user(
            data_product_id,
            current_user,
        )

    @jwt_required()
    @require_roles(
        UserRole.DATA_OWNER,
        UserRole.PLATFORM_ADMIN,
    )
    @data_products_bp.arguments(DataProductUpdateSchema)
    @data_products_bp.response(200, DataProductResponseSchema)
    def patch(self, data, data_product_id):
        current_user = get_current_user()
        return DataProductService.update(
            data_product_id,
            data,
            current_user,
        )
