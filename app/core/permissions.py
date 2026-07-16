# reusable permission logic:

from functools import wraps

from app.core.constants import UserRole
from app.core.exceptions import PermissionDeniedError
from app.core.security import get_current_user


def has_any_role(user, *allowed_roles: UserRole):
    allowed_value = {role.value for role in allowed_roles}
    return user.role in allowed_value


def require_roles(*allowed_user: UserRole):
    def decorator(view_function):
        @wraps(view_function)
        def wrapped_view(*args, **kwargs):
            user = get_current_user()

            if not has_any_role(user, *allowed_user):
                raise PermissionDeniedError(
                    "You do not have permission to perform this action"
                )

            return view_function(*args, **kwargs)

        return wrapped_view

    return decorator
