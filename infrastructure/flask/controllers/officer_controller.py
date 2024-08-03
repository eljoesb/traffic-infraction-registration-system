from flask import Blueprint, request, jsonify
from domain.entities.officer import Officer
from infrastructure.repositories.sqlalchemy_officer_repository import SQLAlchemyOfficerRepository
from infrastructure.config.db_config import db
import logging

logging.basicConfig(level=logging.INFO)

officer_bp = Blueprint('officer', __name__)
officer_repository = SQLAlchemyOfficerRepository(db.session)

@officer_bp.route('/officer', methods=['POST'])
def add_officer():
    logging.info("Adding officer")
    data = request.get_json()
    officer = Officer(name=data['name'], unique_id=data['unique_id'])
    officer_repository.add(officer)
    return jsonify({"message": "Officer added successfully"}), 201

@officer_bp.route('/officer', methods=['GET'])
def get_officer():
    unique_id = request.args.get('unique_id')
    officer = officer_repository.get_by_unique_id(unique_id)
    if officer:
        return jsonify({"name": officer.name, "unique_id": officer.unique_id}), 200
    return jsonify({"error": "Officer not found"}), 404

@officer_bp.route('/officer', methods=['PUT'])
def update_officer():
    unique_id = request.args.get('unique_id')
    data = request.get_json()
    officer = officer_repository.get_by_unique_id(unique_id)
    if officer:
        officer.name = data['name']
        officer.unique_id = data['unique_id']
        officer_repository.update(officer)
        return jsonify({"message": "Officer updated successfully"}), 200
    return jsonify({"error": "Officer not found"}), 404

@officer_bp.route('/officer', methods=['DELETE'])
def delete_officer():
    unique_id = request.args.get('unique_id')
    officer = officer_repository.get_by_unique_id(unique_id)
    if officer:
        officer_repository.delete(officer)
        return jsonify({"message": "Officer deleted successfully"}), 200
    return jsonify({"error": "Officer not found"}), 404

@officer_bp.route('/officers', methods=['GET'])
def get_all_officers():
    officers = officer_repository.get_all()
    result = [{"name": officer.name, "unique_id": officer.unique_id} for officer in officers]
    return jsonify(result), 200
