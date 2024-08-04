from flask_admin.contrib.sqla import ModelView
from flask import flash
from sqlalchemy.exc import SQLAlchemyError
from infrastructure.config.db_config import db

class CustomModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        try:
            super(CustomModelView, self).on_model_change(form, model, is_created)
            flash(f'Successfully {"created" if is_created else "updated"} the record.', 'success')
        except SQLAlchemyError as e:
            db.session.rollback()
            raise

    def on_model_delete(self, model):
        try:
            super(CustomModelView, self).on_model_delete(model)
            flash('Successfully deleted the record.', 'success')
        except SQLAlchemyError as e:
            db.session.rollback()
            raise
