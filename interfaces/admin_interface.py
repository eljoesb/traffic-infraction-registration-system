from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from infrastructure.config.db_config import db, init_db
from domain.entities.person import Person
from domain.entities.vehicle import Vehicle
from domain.entities.officer import Officer
from domain.entities.violation import Violation

app = Flask(__name__)
init_db(app)

admin = Admin(app, name='Traffic Infraction Registration System Admin', template_mode='bootstrap3')

# Add views for each model
admin.add_view(ModelView(Person, db.session))
admin.add_view(ModelView(Vehicle, db.session))
admin.add_view(ModelView(Officer, db.session))

if __name__ == '__main__':
    app.run(debug=True)
