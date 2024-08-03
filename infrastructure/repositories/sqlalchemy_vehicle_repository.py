from domain.repositories.vehicle_repository import VehicleRepository
from domain.entities.vehicle import Vehicle

class SQLAlchemyVehicleRepository(VehicleRepository):
    def __init__(self, session):
        self.session = session

    def add(self, vehicle):
        self.session.add(vehicle)
        self.session.commit()

    def get_by_id(self, vehicle_id):
        return self.session.query(Vehicle).filter_by(id=vehicle_id).first()

    def get_by_license_plate(self, license_plate):
        return self.session.query(Vehicle).filter_by(license_plate=license_plate).first()

    def update(self, vehicle):
        self.session.commit()

    def delete(self, vehicle):
        self.session.delete(vehicle)
        self.session.commit()

    def get_all(self):
        return self.session.query(Vehicle).all()
