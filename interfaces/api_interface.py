from flask import Flask
from infrastructure.config.db_config import init_db, db
from presenters.controllers.violation_controller import violation_bp
from presenters.controllers.person_controller import person_bp
from presenters.controllers.vehicle_controller import vehicle_bp
from presenters.controllers.officer_controller import officer_bp
from presenters.controllers.auth_controller import auth_bp
from presenters.controllers.report_controller import report_bp

from flasgger import Swagger


app = Flask(__name__)
init_db(app)
app.config['DEBUG'] = True

# Register blueprints for controllers
app.register_blueprint(person_bp, url_prefix='/api')
app.register_blueprint(vehicle_bp, url_prefix='/api')
app.register_blueprint(officer_bp, url_prefix='/api')
app.register_blueprint(violation_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(report_bp, url_prefix='/api')

swagger = Swagger(app, template_file='../swagger.yaml')


if __name__ == '__main__':
    app.run(debug=True)
