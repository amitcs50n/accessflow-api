from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

from app.extensions import db
from app.models.organization import Organization
from app.models.user import User
from app.repositories.user_repository import UserRepository


class AuthService:
    @staticmethod
    def register(data):
        organization_data = data["organization"]
        user_data = data["user"]
        email = user_data["email"].strip().lower()
        slug = organization_data["slug"].strip().lower()

        if UserRepository.get_by_email(email):
            abort(409, message="Email already registered")

        existing_organization = db.session.scalar(
            db.select(Organization).where(Organization.slug == slug)
        )
        if existing_organization:
            abort(409, message="Organization slug already exists")

        organization = Organization(name=organization_data["name"].strip(), slug=slug)

        user = User(
            organization=organization,
            name=user_data["name"].strip(),
            email=email,
            password_hash=generate_password_hash(user_data["password"]),
            role="ADMIN",
        )

        try:
            db.session.add(organization)
            UserRepository.add(user)
            db.session.commit()

        except IntegrityError:
            db.session.rollback()
            abort(409, message="Registration details already exist")

        return {
            "message": "User registered successfully",
            "organization": organization,
            "user": user,
        }

    #   This service performs the complete registration workflow:
    #   checks duplicates, normalizes values, hashes the password,
    #   creates both records, and commits them together
    @staticmethod
    def login(data):
        email = data["email"].strip().lower()
        user = UserRepository.get_by_email(email)

        if user is None or not check_password_hash(
            user.password_hash, data["password"]
        ):
            abort(401, message="Invalid email or password")

        if not user.is_active:
            abort(403, message="User account is inactive")

        access_token = create_access_token(identity=str(user.id))

        return {
            "access_token": access_token,
            "token_type": "Bearer",
        }
