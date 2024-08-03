from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.config.db_config import db

class Vehicle(db.Model):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key=True)
    license_plate = Column(String(10), unique=True, nullable=False)
    brand = Column(String(50), nullable=False)
    color = Column(String(50), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'), nullable=False)

    person = relationship('Person', back_populates='vehicles')
    violations = relationship('Violation', back_populates='vehicle', cascade="all, delete-orphan")

    def __init__(self, license_plate, brand, color, person_id):
        self.license_plate = license_plate
        self.brand = brand
        self.color = color
        self.person_id = person_id
