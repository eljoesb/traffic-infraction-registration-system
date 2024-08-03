from sqlalchemy import Column, Integer, String
from datetime import datetime, timedelta
import jwt
import os
from dotenv import load_dotenv
from infrastructure.config.db_config import db

# Cargar variables de entorno desde el archivo .env
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

class Officer(db.Model):
    __tablename__ = 'officers'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    unique_id = Column(String(50), unique=True, nullable=False)

    def __init__(self, name, unique_id):
        self.name = name
        self.unique_id = unique_id

    def generate_token(self, expires_in=3600):
        exp = datetime.utcnow() + timedelta(seconds=expires_in)
        token = jwt.encode({'id': self.id, 'exp': exp}, SECRET_KEY, algorithm='HS256')
        return token

    @staticmethod
    def verify_token(token):
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return data['id']
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
