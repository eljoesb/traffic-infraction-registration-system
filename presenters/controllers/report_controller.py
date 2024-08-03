from flask import Blueprint, request, jsonify
from infrastructure.repositories.sqlalchemy_person_repository import SQLAlchemyPersonRepository
from infrastructure.repositories.sqlalchemy_violation_repository import SQLAlchemyViolationRepository
from infrastructure.repositories.sqlalchemy_vehicle_repository import SQLAlchemyVehicleRepository
from infrastructure.config.db_config import db

report_bp = Blueprint('report', __name__)
person_repository = SQLAlchemyPersonRepository(db.session)
violation_repository = SQLAlchemyViolationRepository(db.session)
vehicle_repository = SQLAlchemyVehicleRepository(db.session)

@report_bp.route('/generar_informe', methods=['GET'])
def generar_informe():
    email = request.args.get('email')
    person = person_repository.get_by_email(email)
    if not person:
        return jsonify({'error': 'Person not found'}), 404

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

    return jsonify({'violations': violations}), 200
