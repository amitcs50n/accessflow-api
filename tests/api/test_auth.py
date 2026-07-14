from unittest.mock import patch

from app import create_app


def create_test_client():
    app = create_app(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
            "JWT_SECRET_KEY": "test-secret",
        }
    )
    return app.test_client()


@patch("app.routes.auth.AuthService.register")
def test_registration_endpoint(mock_register):
    mock_register.return_value = {
        "message": "User registered successfully",
        "organization": {
            "id": 1,
            "name": "Test Organization",
            "slug": "test-organization",
        },
        "user": {
            "id": 1,
            "name": "Test User",
            "email": "test@example.com",
            "role": "ADMIN",
        },
    }

    client = create_test_client()

    response = client.post(
        "/api/v1/auth/register",
        json={
            "organization": {
                "name": "Test Organization",
                "slug": "test-organization",
            },
            "user": {
                "name": "Test User",
                "email": "test@example.com",
                "password": "SecurePass123",
            },
        },
    )

    body = response.get_json()

    assert response.status_code == 201
    assert body["message"] == "User registered successfully"
    assert body["user"]["email"] == "test@example.com"
    assert "password" not in body["user"]
    assert "password_hash" not in body["user"]
    mock_register.assert_called_once()


@patch("app.routes.auth.AuthService.login")
def test_login_endpoint(mock_login):
    mock_login.return_value = {
        "access_token": "test-jwt-token",
        "token_type": "Bearer",
    }

    client = create_test_client()

    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "test@example.com",
            "password": "SecurePass123",
        },
    )

    body = response.get_json()

    assert response.status_code == 200
    assert body["access_token"] == "test-jwt-token"
    assert body["token_type"] == "Bearer"
    assert "password" not in body
    mock_login.assert_called_once()
