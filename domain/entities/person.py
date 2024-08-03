from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from infrastructure.config.db_config import db

class Person(db.Model):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)

    vehicles = relationship('Vehicle', back_populates='person', cascade="all, delete-orphan")

    def __init__(self, name, email):
        self.name = name
        self.email = email
