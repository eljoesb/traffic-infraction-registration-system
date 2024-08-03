from flask import Blueprint, request, jsonify
from application.use_cases.register_violation import RegisterViolation
from domain.services.violation_service import ViolationService
from infrastructure.repositories.sqlalchemy_violation_repository import SQLAlchemyViolationRepository
from infrastructure.repositories.sqlalchemy_vehicle_repository import SQLAlchemyVehicleRepository
from infrastructure.config.db_config import db

violation_bp = Blueprint('violation', __name__)
violation_repository = SQLAlchemyViolationRepository(db.session)
vehicle_repository = SQLAlchemyVehicleRepository(db.session)
violation_service = ViolationService(violation_repository, vehicle_repository)
register_violation_use_case = RegisterViolation(violation_service)

@violation_bp.route('/register_violation', methods=['POST'])
def register_violation():
    data = request.get_json()
    try:
        violation = register_violation_use_case.execute(
            data['license_plate'],
            data['timestamp'],
            data['comments']
        )
        return jsonify({"message": "Violation registered successfully"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": "Unexpected error"}), 500
