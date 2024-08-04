from flask import Flask, render_template
from flask_admin import Admin
from infrastructure.config.db_config import db, init_db
from domain.entities.person import Person
from domain.entities.vehicle import Vehicle
from domain.entities.officer import Officer
from domain.entities.violation import Violation
from presenters.views.custom_view import CustomModelView
from presenters.views.vehicle_view import VehicleModelView
from presenters.views.violation_view import ViolationModelView
from presenters.views.person_view import PersonModelView
import logging

# Configurar el logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necesario para usar flash messages

try:
    init_db(app)
except Exception as e:
    logger.error("Error initializing database: %s", e)
    raise

admin = Admin(app, name='Traffic Infraction Registration System Admin', template_mode='bootstrap3')

# Add views for each model
admin.add_view(PersonModelView(Person, db.session))
admin.add_view(VehicleModelView(Vehicle, db.session))
admin.add_view(CustomModelView(Officer, db.session))
admin.add_view(ViolationModelView(Violation, db.session))


@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', message='An unexpected error occurred. Please try again later.'), 500

if __name__ == '__main__':
    app.run(debug=True)
