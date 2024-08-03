from flask import Blueprint, request, jsonify
from domain.entities.person import Person
from infrastructure.repositories.sqlalchemy_person_repository import SQLAlchemyPersonRepository
from infrastructure.config.db_config import db
import logging

logging.basicConfig(level=logging.DEBUG)

person_bp = Blueprint('person', __name__)
person_repository = SQLAlchemyPersonRepository(db.session)

@person_bp.route('/person', methods=['POST'])
def add_person():
    try:
        data = request.get_json()
        person = Person(name=data['name'], email=data['email'])
        person_repository.add(person)
        return jsonify({"message": "Person added successfully"}), 201
    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({"error": "Error adding person"}), 500

@person_bp.route('/person', methods=['GET'])
def get_person():
    email = request.args.get('email')
    person = person_repository.get_by_email(email)
    logging.info(f"Person found: {person.email}")
    if person:
        return jsonify({"id": person.id, "name": person.name, "email": person.email}), 200
    return jsonify({"error": "Person not found"}), 404

@person_bp.route('/person', methods=['PUT'])
def update_person():
    email = request.args.get('email')
    data = request.get_json()
    person = person_repository.get_by_email(email)
    if person:
        person.name = data['name']
        person.email = data['email']
        person_repository.update(person)
        return jsonify({"message": "Person updated successfully"}), 200
    return jsonify({"error": "Person not found"}), 404

@person_bp.route('/person', methods=['DELETE'])
def delete_person():
    email = request.args.get('email')
    person = person_repository.get_by_email(email)
    if person:
        person_repository.delete(person)
        return jsonify({"message": "Person deleted successfully"}), 200
    return jsonify({"error": "Person not found"}), 404
