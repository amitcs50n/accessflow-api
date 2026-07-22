from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from app.core.constants import UserRole
from app.core.permissions import require_roles
from app.core.security import get_current_user
from app.schemas.access_request import (
    AccessRequestCreateSchema,
    AccessRequestResponseSchema,
)
from app.services.access_request_service import AccessRequestService


access_requests_bp = Blueprint(
    "access_requests",
    __name__,
    url_prefix="/api/v1/access-requests",
    description="Access request operations",
)


@access_requests_bp.route("")
class AccessRequestListView(MethodView):
    @jwt_required()
    @access_requests_bp.response(200, AccessRequestResponseSchema(many=True))
    def get(self):
        current_user = get_current_user()
        return AccessRequestService.list_for_user(current_user)

    @jwt_required()
    @require_roles(
        UserRole.REQUESTER,
        UserRole.MANAGER,
        UserRole.DATA_OWNER,
        UserRole.PLATFORM_ADMIN,
    )
    @access_requests_bp.arguments(AccessRequestCreateSchema)
    @access_requests_bp.response(201, AccessRequestResponseSchema)
    def post(self, data):
        current_user = get_current_user()
        return AccessRequestService.create(data, current_user)


@access_requests_bp.route("/<int:access_request_id>")
class AccessRequestView(MethodView):
    @jwt_required()
    @access_requests_bp.response(200, AccessRequestResponseSchema)
    def get(self, access_request_id):
        current_user = get_current_user()
        return AccessRequestService.get_for_user(
            access_request_id,
            current_user,
        )
