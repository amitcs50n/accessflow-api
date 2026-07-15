class NotFoundError(Exception):
    """Raised when a requested resource does not exist."""


class PermissionDeniedError(Exception):
    """Raised when a user cannot perform an action."""


class ConflictError(Exception):
    """Raised when data conflicts with an existing resource."""


def _error_response(code, message):
    return {
        "error": {
            "code": code,
            "message": message,
        }
    }


def register_error_handlers(app):
    @app.errorhandler(NotFoundError)
    def handle_not_found(error):
        return _error_response("Not found", str(error)), 404

    @app.errorhandler(PermissionDeniedError)
    def handle_permission_denied(error):
        return _error_response("permission_denied", str(error)), 403

    @app.errorhandler(ConflictError)
    def handle_conflict(error):
        return _error_response("conflict", str(error)), 409
