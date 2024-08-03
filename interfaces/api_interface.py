from flask import Flask
from infrastructure.config.db_config import init_db
from infrastructure.flask.controllers.violation_controller import violation_bp
from infrastructure.flask.controllers.person_controller import person_bp
from infrastructure.flask.controllers.vehicle_controller import vehicle_bp
from infrastructure.flask.controllers.officer_controller import officer_bp
from infrastructure.flask.controllers.auth_controller import auth_bp
from infrastructure.flask.controllers.report_controller import report_bp

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

if __name__ == '__main__':
    app.run(debug=True)
