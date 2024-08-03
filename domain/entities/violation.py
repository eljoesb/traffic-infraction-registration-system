from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from infrastructure.config.db_config import db

class Violation(db.Model):
    __tablename__ = 'violations'

    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    comments = Column(String(200), nullable=False)

    vehicle = relationship('Vehicle', back_populates='violations')

    def __init__(self, vehicle_id, timestamp, comments):
        self.vehicle_id = vehicle_id
        self.timestamp = timestamp
        self.comments = comments
