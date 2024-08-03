from flask import Blueprint, request, jsonify
from domain.entities.violation import Violation
from domain.entities.officer import Officer
from infrastructure.repositories.sqlalchemy_violation_repository import SQLAlchemyViolationRepository
from infrastructure.repositories.sqlalchemy_vehicle_repository import SQLAlchemyVehicleRepository
from infrastructure.config.db_config import db

violation_bp = Blueprint('violation', __name__)
violation_repository = SQLAlchemyViolationRepository(db.session)
vehicle_repository = SQLAlchemyVehicleRepository(db.session)

def token_required(f):
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token:
            token = token.split(" ")[1]
            officer_id = Officer.verify_token(token)
            if officer_id:
                return f(officer_id, *args, **kwargs)
        return jsonify({'error': 'Unauthorized'}), 401
    return decorator

@violation_bp.route('/violation', methods=['POST'])
@token_required
def add_violation(officer_id):
    data = request.get_json()
    vehicle = vehicle_repository.get_by_license_plate(data['license_plate'])
    if vehicle:
        violation = Violation(
            vehicle_id=vehicle.id,
            timestamp=data['timestamp'],
            comments=data['comments']
        )
        violation_repository.add(violation)
        return jsonify({"message": "Violation added successfully"}), 201
    return jsonify({"error": "Vehicle not found"}), 404
