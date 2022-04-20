import datetime

from passlib.hash import pbkdf2_sha256 as sha256
from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey

from app.database.database import base, session


class UserModel(base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(30), nullable=False)
    hashed_password = Column(String(50), nullable=False)

    @classmethod
    def find_by_id(cls, user_id, to_dict=True):
        """
        A function that finds a user by his id from the 'users' table
        """
        user = session.query(cls).filter_by(user_id=user_id).first()
        if not user:
            return {}
        if to_dict:
            return cls.to_dict(user)
        else:
            return user

    @classmethod
    def find_by_email(cls, email, to_dict=True):
        """
        A function that finds a user by his email from the 'users' table
        """
        user = session.query(cls).filter_by(email=email).first()
        if not user:
            return {}
        if to_dict:
            return cls.to_dict(user)
        else:
            return user

    @classmethod
    def return_all(cls):
        """
        A function that returns all users from the 'users' table
        """
        users = session.query(cls).order_by(cls.user_id).all()
        return [cls.to_dict(user) for user in users]

    @classmethod
    def delete_by_id(cls, user_id):
        """
        A function that allows to delete a user from the 'users' table by his id
        """
        user = session.query(cls).filter_by(user_id=user_id).first()
        if user:
            session.delete(user)
            session.commit()
            return 200
        else:
            return 404

    def save_to_db(self):
        session.add(self)
        session.commit()

    @staticmethod
    def to_dict(user):
        """
        A function that converts data into dict for better readability
        """
        return {
            "id": user.user_id,
            "name": user.name,
            "age": user.age,
            "email": user.email,
        }

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, some_hash):
        return sha256.verify(password, some_hash)
