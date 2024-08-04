from wtforms.fields import SelectField
from wtforms.validators import DataRequired
from domain.entities.vehicle import Vehicle
from flask import flash
from domain.entities.person import Person
from presenters.views.custom_view import CustomModelView
from infrastructure.config.db_config import db
from infrastructure.repositories.sqlalchemy_vehicle_repository import SQLAlchemyVehicleRepository
from infrastructure.repositories.sqlalchemy_person_repository import SQLAlchemyPersonRepository
import logging

logging.basicConfig(level=logging.DEBUG)

vehicle_repository = SQLAlchemyVehicleRepository(db.session)
person_repository = SQLAlchemyPersonRepository(db.session)

class VehicleModelView(CustomModelView):
    form_extra_fields = {
        'person_email': SelectField('Person Email', choices=[], validators=[DataRequired()])
    }

    def on_form_prefill(self, form, id):
        form.person_email.choices = [(p.email, p.email) for p in Person.query.all()]
        super(VehicleModelView, self).on_form_prefill(form, id)

    def create_form(self, obj=None):
        form = super(VehicleModelView, self).create_form(obj)
        form.person_email.choices = [(p.email, p.email) for p in Person.query.all()]
        return form

    def edit_form(self, obj=None):
        form = super(VehicleModelView, self).edit_form(obj)
        form.person_email.choices = [(p.email, p.email) for p in Person.query.all()]
        return form

    def create_model(self, form):
        person = person_repository.get_by_email(form.person_email.data)
        if person:
            logging.debug(f"Found person: {person.name} with ID {person.id}")
            vehicle = Vehicle(
                license_plate=form.license_plate.data,
                brand=form.brand.data,
                color=form.color.data,
                person_id=person.id
            )
            try:
                vehicle_repository.add(vehicle)
                logging.info(f"Vehicle added: {vehicle.license_plate}")
                flash('Vehicle created successfully!', 'success')
            except Exception as e:
                logging.error(f"Error adding vehicle: {e}")
                flash('Failed to create vehicle.', 'danger')
        else:
            flash('Failed to create vehicle. Person not found.', 'danger')

    def update_model(self, form, model):
        person = person_repository.get_by_email(form.person_email.data)
        if person:
            vehicle = vehicle_repository.get_by_license_plate(model.license_plate)
            if vehicle:
                vehicle.license_plate = form.license_plate.data
                vehicle.brand = form.brand.data
                vehicle.color = form.color.data
                vehicle.person_id = person.id
                try:
                    vehicle_repository.update(vehicle)
                    logging.info(f"Vehicle updated: {vehicle.license_plate}")
                    flash('Vehicle updated successfully!', 'success')
                except Exception as e:
                    logging.error(f"Error updating vehicle: {e}")
                    flash('Failed to update vehicle.', 'danger')
            else:
                flash('Failed to update vehicle. Vehicle not found.', 'danger')
        else:
            flash('Failed to update vehicle. Person not found.', 'danger')

    def delete_model(self, model):
        vehicle = vehicle_repository.get_by_license_plate(model.license_plate)
        if vehicle:
            try:
                vehicle_repository.delete(vehicle)
                logging.info(f"Vehicle deleted: {vehicle.license_plate}")
                flash('Vehicle deleted successfully!', 'success')
            except Exception as e:
                logging.error(f"Error deleting vehicle: {e}")
                flash('Failed to delete vehicle.', 'danger')
        else:
            flash('Failed to delete vehicle. Vehicle not found.', 'danger')
