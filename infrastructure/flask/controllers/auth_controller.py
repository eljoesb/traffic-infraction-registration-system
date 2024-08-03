from flask import Blueprint, request, jsonify
from domain.entities.officer import Officer
from infrastructure.repositories.sqlalchemy_officer_repository import SQLAlchemyOfficerRepository
from infrastructure.config.db_config import db

auth_bp = Blueprint('auth', __name__)
officer_repository = SQLAlchemyOfficerRepository(db.session)

@auth_bp.route('/token', methods=['POST'])
def generate_token():
    data = request.get_json()
    unique_id = data.get('unique_id')
    officer = officer_repository.get_by_unique_id(unique_id)
    if officer:
        token = officer.generate_token()
        return jsonify({'token': token}), 200
    return jsonify({'error': 'Invalid unique ID'}), 401
