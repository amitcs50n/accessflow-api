from types import SimpleNamespace
from unittest.mock import patch

from flask_jwt_extended import create_access_token

from app import create_app
from app.core.constants import UserRole


def create_test_client_and_token():
    app = create_app(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
            "JWT_SECRET_KEY": "test-secret",
        }
    )

    with app.app_context():
        token = create_access_token(identity="1")

    return app.test_client(), token


@patch("app.core.permissions.get_current_user")
def test_requester_cannot_access_admin_check(mock_get_current_user):
    mock_get_current_user.return_value = SimpleNamespace(role=UserRole.REQUESTER.value)
    client, token = create_test_client_and_token()

    response = client.get(
        "/api/v1/users/admin-check",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 403
    assert response.get_json() == {
        "error": {
            "code": "permission_denied",
            "message": "You do not have permission to perform this action",
        }
    }


@patch("app.core.permissions.get_current_user")
def test_platform_admin_can_access_admin_check(mock_get_current_user):
    mock_get_current_user.return_value = SimpleNamespace(
        role=UserRole.PLATFORM_ADMIN.value
    )
    client, token = create_test_client_and_token()

    response = client.get(
        "/api/v1/users/admin-check",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert response.get_json() == {
        "message": "Platform admin access granted",
    }
