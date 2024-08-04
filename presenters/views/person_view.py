
from flask import flash
from presenters.views.custom_view import CustomModelView
from infrastructure.config.db_config import db
from infrastructure.repositories.sqlalchemy_vehicle_repository import SQLAlchemyVehicleRepository
from infrastructure.repositories.sqlalchemy_violation_repository import SQLAlchemyViolationRepository
from infrastructure.repositories.sqlalchemy_person_repository import SQLAlchemyPersonRepository
from flask_admin.actions import action
import logging

logging.basicConfig(level=logging.DEBUG)
violation_repository = SQLAlchemyViolationRepository(db.session)
vehicle_repository = SQLAlchemyVehicleRepository(db.session)
person_repository = SQLAlchemyPersonRepository(db.session)


class PersonModelView(CustomModelView):
    @action('generate_report', 'Generar Reporte de Infracciones', 'Estas seguro que quieres ver el reporte de esta persona?')
    def action_generate_report(self, ids):
        try:
            for person_id in ids:
                person = self.get_one(person_id)
                email = person.email
                violations_report = self.generate_report(email)
                flash(f'Report generated for {person.name}: {violations_report}', 'success')
        except Exception as ex:
            if not self.handle_view_exception(ex):
                raise
            flash(f'Failed to generate report. {str(ex)}', 'error')

    def generate_report(self, email):
        person = person_repository.get_by_email(email)
        if not person:
            return 'Person not found'

        vehicles = person.vehicles
        vehicle_ids = [vehicle.id for vehicle in vehicles]
        violations = []
        for vehicle_id in vehicle_ids:
            vehicle_violations = violation_repository.get_by_vehicle_id(vehicle_id)
            vehicle = vehicle_repository.get_by_id(vehicle_id)
            for violation in vehicle_violations:
                violations.append({
                    'vehicle_id': vehicle.id,
                    'license_plate': vehicle.license_plate,
                    'timestamp': violation.timestamp.isoformat(),
                    'comments': violation.comments
                })
        return violations
