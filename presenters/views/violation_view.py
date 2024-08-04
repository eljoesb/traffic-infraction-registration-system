from wtforms.fields import StringField, DateTimeLocalField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask import flash
from domain.entities.violation import Violation
from domain.entities.vehicle import Vehicle
from domain.entities.officer import Officer
from presenters.views.custom_view import CustomModelView
from infrastructure.config.db_config import db
from infrastructure.repositories.sqlalchemy_violation_repository import SQLAlchemyViolationRepository
from infrastructure.repositories.sqlalchemy_vehicle_repository import SQLAlchemyVehicleRepository
from infrastructure.repositories.sqlalchemy_officer_repository import SQLAlchemyOfficerRepository
import logging

logging.basicConfig(level=logging.DEBUG)

violation_repository = SQLAlchemyViolationRepository(db.session)
vehicle_repository = SQLAlchemyVehicleRepository(db.session)
officer_repository = SQLAlchemyOfficerRepository(db.session)

class ViolationModelView(CustomModelView):
    form_extra_fields = {
        'license_plate': SelectField('Vehicle License Plate', choices=[], validators=[DataRequired()]),
        'timestamp': DateTimeLocalField('Timestamp', format='%Y-%m-%dT%H:%M', validators=[DataRequired()]),
        'comments': TextAreaField('Comments', validators=[DataRequired()]),
        'officer_id': SelectField('Officer', choices=[], validators=[DataRequired()])
    }

    def on_form_prefill(self, form, id):
        form.license_plate.choices = [(v.license_plate, v.license_plate) for v in Vehicle.query.all()]
        form.officer_id.choices = [(o.id, o.name) for o in Officer.query.all()]
        super(ViolationModelView, self).on_form_prefill(form, id)

    def create_form(self, obj=None):
        form = super(ViolationModelView, self).create_form(obj)
        form.license_plate.choices = [(v.license_plate, v.license_plate) for v in Vehicle.query.all()]
        form.officer_id.choices = [(o.id, o.name) for o in Officer.query.all()]
        return form

    def edit_form(self, obj=None):
        form = super(ViolationModelView, self).edit_form(obj)
        form.license_plate.choices = [(v.license_plate, v.license_plate) for v in Vehicle.query.all()]
        form.officer_id.choices = [(o.id, o.name) for o in Officer.query.all()]
        return form

    def create_model(self, form):
        vehicle = vehicle_repository.get_by_license_plate(form.license_plate.data)
        officer = officer_repository.get_by_id(form.officer_id.data)
        if officer:
            token = officer.generate_token()
            if token:
                if vehicle:
                    violation = Violation(
                        vehicle_id=vehicle.id,
                        timestamp=form.timestamp.data,
                        comments=form.comments.data
                    )
                    try:
                        violation_repository.add(violation)
                        flash('Violation created successfully!', 'success')
                    except Exception as e:
                        logging.error(f"Error adding violation: {e}")
                        flash('Failed to create violation.', 'danger')
                else:
                    flash('Failed to create violation. Vehicle not found.', 'danger')
            else:
                flash('Failed to generate token.', 'danger')
        else:
            flash('Failed to create violation. Officer not found.', 'danger')
