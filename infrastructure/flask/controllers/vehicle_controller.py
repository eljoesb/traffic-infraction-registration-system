from flask import Blueprint, request, jsonify
from domain.entities.vehicle import Vehicle
from domain.entities.person import Person
from infrastructure.repositories.sqlalchemy_vehicle_repository import SQLAlchemyVehicleRepository
from infrastructure.repositories.sqlalchemy_person_repository import SQLAlchemyPersonRepository
from infrastructure.config.db_config import db
import logging

vehicle_bp = Blueprint('vehicle', __name__)
vehicle_repository = SQLAlchemyVehicleRepository(db.session)
person_repository = SQLAlchemyPersonRepository(db.session)

logging.basicConfig(level=logging.DEBUG)

@vehicle_bp.route('/vehicle', methods=['POST'])
def add_vehicle():
    data = request.get_json()
    person = person_repository.get_by_email(data['email'])
    if person:
        vehicle = Vehicle(
            license_plate=data['license_plate'],
            brand=data['brand'],
            color=data['color'],
            person_id=person.id
        )
        vehicle_repository.add(vehicle)
        logging.info(f"Vehicle added: {vehicle.license_plate}")
        return jsonify({"message": "Vehicle added successfully"}), 201
    return jsonify({"error": "Person not found"}), 404

@vehicle_bp.route('/vehicle', methods=['GET'])
def get_vehicle():
    license_plate = request.args.get('license_plate')
    vehicle = vehicle_repository.get_by_license_plate(license_plate)
    if vehicle:
        person = person_repository.get_by_id(vehicle.person_id)
        return jsonify({
            "license_plate": vehicle.license_plate,
            "brand": vehicle.brand,
            "color": vehicle.color,
            "email": person.email
        }), 200
    return jsonify({"error": "Vehicle not found"}), 404

@vehicle_bp.route('/vehicle', methods=['PUT'])
def update_vehicle():
    license_plate = request.args.get('license_plate')
    data = request.get_json()
    vehicle = vehicle_repository.get_by_license_plate(license_plate)
    person = person_repository.get_by_email(data['email'])
    if vehicle and person:
        vehicle.license_plate = data['license_plate']
        vehicle.brand = data['brand']
        vehicle.color = data['color']
        vehicle.person_id = person.id
        vehicle_repository.update(vehicle)
        return jsonify({"message": "Vehicle updated successfully"}), 200
    return jsonify({"error": "Vehicle or person not found"}), 404

@vehicle_bp.route('/vehicle', methods=['DELETE'])
def delete_vehicle():
    license_plate = request.args.get('license_plate')
    vehicle = vehicle_repository.get_by_license_plate(license_plate)
    if vehicle:
        vehicle_repository.delete(vehicle)
        return jsonify({"message": "Vehicle deleted successfully"}), 200
    return jsonify({"error": "Vehicle not found"}), 404

@vehicle_bp.route('/vehicles', methods=['GET'])
def get_all_vehicles():
    vehicles = vehicle_repository.get_all()
    result = []
    for vehicle in vehicles:
        person = person_repository.get_by_id(vehicle.person_id)
        result.append({
            "license_plate": vehicle.license_plate,
            "brand": vehicle.brand,
            "color": vehicle.color,
            "email": person.email
        })
    return jsonify(result), 200
