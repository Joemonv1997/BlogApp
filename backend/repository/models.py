import jwt
import datetime
import os
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime,Boolean
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from database import database_integration

Base, Session, engine = database_integration()
SECRET_KEY = os.environ["SECRET_KEY"]
class User(UserMixin,Base):
    __tablename__="User"
    id=Column(Integer,primary_key=True,index=True)
    user_name=Column(String(100),unique=True,nullable=False)
    first_name=Column(String(100),nullable=True)
    middle_name=Column(String(100),nullable=True)
    last_name=Column(String(100),nullable=True)
    email_address=Column(String(200),unique=True,nullable=False)
    password=Column(String(100),nullable=False)
    is_admin=Column(Boolean,nullable=False)

    def __init__(self,user_name,password,first_name,last_name,middle_name,email_address) -> None:
        self.user_name=user_name
        self.password=generate_password_hash(password)
        self.first_name=first_name
        self.middle_name=middle_name
        self.last_name=last_name
        self.email_address=email_address
    
    def __repr__(self) -> str:
        return f"User {self.email_address}"
    
    def verify_password(self,check_password):
        return check_password_hash(self.password,check_password)

    def encode_auth_token(self, user_id):
        try:
            payload = {
                "exp": datetime.datetime.utcnow()
                + datetime.timedelta(days=0, seconds=500000),
                "iat": datetime.datetime.utcnow(),
                "userid": user_id,
                }
            return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        except Exception as e:
            return e
    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, SECRET_KEY)
            return True, payload["userid"]
        except jwt.ExpiredSignatureError:
            return False, "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return False, "Invalid token. Please log in again."

class TokenStore(Base):
    __tablename__ = "tokenstore"
    id = Column(Integer, primary_key=True, autoincrement=True)
    token = Column(String, unique=True, nullable=False)
    blacklisted_on = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("User.id", ondelete='CASCADE'))
    def __init__(self, token, user_id):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()
        self.user_id = user_id
    def __repr__(self):
        return "<id: UserID: {}".format(self.user_id)