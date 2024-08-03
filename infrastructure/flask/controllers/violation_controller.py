from flask import Blueprint, request, jsonify
from domain.entities.violation import Violation
from infrastructure.repositories.sqlalchemy_violation_repository import SQLAlchemyViolationRepository
from infrastructure.repositories.sqlalchemy_vehicle_repository import SQLAlchemyVehicleRepository
from infrastructure.config.db_config import db

violation_bp = Blueprint('violation', __name__)
violation_repository = SQLAlchemyViolationRepository(db.session)
vehicle_repository = SQLAlchemyVehicleRepository(db.session)

@violation_bp.route('/violation', methods=['POST'])
def add_violation():
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

@violation_bp.route('/violation/<int:id>', methods=['GET'])
def get_violation(id):
    violation = violation_repository.get_by_id(id)
    if violation:
        return jsonify({
            "vehicle_id": violation.vehicle_id,
            "timestamp": violation.timestamp.isoformat(),
            "comments": violation.comments
        }), 200
    return jsonify({"error": "Violation not found"}), 404

@violation_bp.route('/violation/<int:id>', methods=['PUT'])
def update_violation(id):
    data = request.get_json()
    violation = violation_repository.get_by_id(id)
    if violation:
        violation.timestamp = data['timestamp']
        violation.comments = data['comments']
        violation_repository.update(violation)
        return jsonify({"message": "Violation updated successfully"}), 200
    return jsonify({"error": "Violation not found"}), 404

@violation_bp.route('/violation/<int:id>', methods=['DELETE'])
def delete_violation(id):
    violation = violation_repository.get_by_id(id)
    if violation:
        violation_repository.delete(violation)
        return jsonify({"message": "Violation deleted successfully"}), 200
    return jsonify({"error": "Violation not found"}), 404

@violation_bp.route('/violations', methods=['GET'])
def get_all_violations():
    violations = violation_repository.get_all()
    result = [{
        "vehicle_id": violation.vehicle_id,
        "timestamp": violation.timestamp.isoformat(),
        "comments": violation.comments
    } for violation in violations]
    return jsonify(result), 200
