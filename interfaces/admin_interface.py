from flask import Flask, render_template, redirect, url_for, flash
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from infrastructure.config.db_config import db, init_db
from domain.entities.person import Person
from domain.entities.vehicle import Vehicle
from domain.entities.officer import Officer
from domain.entities.violation import Violation
from sqlalchemy.exc import SQLAlchemyError
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

class CustomModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        try:
            super(CustomModelView, self).on_model_change(form, model, is_created)
            # Flash a success message and redirect
            flash(f'Successfully {"created" if is_created else "updated"} the record.', 'success')
            return redirect(url_for('.index_view'))
        except SQLAlchemyError as e:
            db.session.rollback()
            # Log the error and show a user-friendly message
            app.logger.error(f'Error while { "creating" if is_created else "updating" } record: {e}')
            return render_template('error.html', message=f'An error occurred while { "creating" if is_created else "updating" } the record. Please try again later.')

    def on_model_delete(self, model):
        try:
            super(CustomModelView, self).on_model_delete(model)
            # Flash a success message and redirect
            flash('Successfully deleted the record.', 'success')
            return redirect(url_for('.index_view'))
        except SQLAlchemyError as e:
            db.session.rollback()
            # Log the error and show a user-friendly message
            app.logger.error(f'Error while deleting record: {e}')
            return render_template('error.html', message='An error occurred while deleting the record. Please try again later.')

# Add views for each model
admin.add_view(CustomModelView(Person, db.session))
admin.add_view(CustomModelView(Vehicle, db.session))
admin.add_view(CustomModelView(Officer, db.session))
admin.add_view(CustomModelView(Violation, db.session))

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', message='An unexpected error occurred. Please try again later.'), 500

if __name__ == '__main__':
    app.run(debug=True)
