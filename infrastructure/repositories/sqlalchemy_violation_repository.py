from domain.repositories.violation_repository import ViolationRepository
from domain.entities.violation import Violation

class SQLAlchemyViolationRepository(ViolationRepository):
    def __init__(self, session):
        self.session = session

    def add(self, violation):
        self.session.add(violation)
        self.session.commit()

    def get_by_id(self, violation_id):
        return self.session.query(Violation).filter_by(id=violation_id).first()

    def update(self, violation):
        self.session.commit()

    def delete(self, violation):
        self.session.delete(violation)
        self.session.commit()

    def get_all(self):
        return self.session.query(Violation).all()

    def get_by_vehicle_id(self, vehicle_id):
        return self.session.query(Violation).filter_by(vehicle_id=vehicle_id).all()
