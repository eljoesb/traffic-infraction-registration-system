
from domain.entities.violation import Violation

class ViolationService:
    def __init__(self, violation_repository, vehicle_repository):
        self.violation_repository = violation_repository
        self.vehicle_repository = vehicle_repository

    def register_violation(self, license_plate, timestamp, comments):
        vehicle = self.vehicle_repository.get_by_license_plate(license_plate)
        if not vehicle:
            raise ValueError("Vehicle not found")
        violation = Violation(vehicle, timestamp, comments)
        self.violation_repository.add(violation)
        return violation
