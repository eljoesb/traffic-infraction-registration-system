class RegisterViolation:
    def __init__(self, violation_service):
        self.violation_service = violation_service

    def execute(self, license_plate, timestamp, comments):
        return self.violation_service.register_violation(license_plate, timestamp, comments)
