from flask.views import MethodView
from flask_smorest import Blueprint

from app.schemas.auth import (
    RegisterSchema,
    RegisterResponseSchema,
    LoginResponseSchema,
    LoginSchema,
)
from app.services.auth_service import AuthService

auth_bp = Blueprint(
    "auth", __name__, url_prefix="/api/v1/auth", description="Authentication operations"
)


@auth_bp.route("/register")
class RegisterView(MethodView):
    @auth_bp.arguments(RegisterSchema)  # validates JSON
    @auth_bp.response(201, RegisterResponseSchema)  # formats the response
    def post(self, data):  #  receives validated data
        return AuthService.register(data)  # performs the business logic


@auth_bp.route("/login")
class Login_view(MethodView):
    @auth_bp.arguments(LoginSchema)
    @auth_bp.response(200, LoginResponseSchema)
    def post(self, data):
        return AuthService.login(data)
