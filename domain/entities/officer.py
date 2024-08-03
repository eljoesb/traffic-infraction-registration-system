from sqlalchemy import Column, Integer, String
from infrastructure.config.db_config import db

class Officer(db.Model):
    __tablename__ = 'officers'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    unique_id = Column(String(50), unique=True, nullable=False)

    def __init__(self, name, unique_id):
        self.name = name
        self.unique_id = unique_id
