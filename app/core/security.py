from flask_jwt_extended import get_jwt_identity
from flask_smorest import abort

from app.repositories.user_repository import UserRepository


def get_current_user():
    identity = get_jwt_identity()

    try:
        user_id = int(identity)
    except (TypeError, ValueError):
        abort(401, message="Invalid authentication credentials")

    user = UserRepository.get_by_id(user_id)

    if user is None or not user.is_active:
        abort(401, message="Invalid authentication credentials")

    return user
