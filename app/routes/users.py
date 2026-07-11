from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint

from app.core.security import get_current_user
from app.schemas.auth import PlainUserSchema

users_bp = Blueprint(
    "users", __name__, url_prefix="/api/v1/users", description="User operations"
)


@users_bp.route("/me")
class CurrentUserView(MethodView):
    @jwt_required()
    @users_bp.response(200, PlainUserSchema)
    def get(self):
        return get_current_user()
