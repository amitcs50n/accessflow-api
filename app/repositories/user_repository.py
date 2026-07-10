from app.extensions import db
from app.models.user import User


class UserRepository:
    @staticmethod
    def get_by_email(email):
        statement = db.select(User).where(User.email == email)
        return db.session.scalar(statement)

    @staticmethod
    def add(user):
        db.session.add(user)
