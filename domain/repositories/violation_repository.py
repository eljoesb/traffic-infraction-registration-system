class ViolationRepository:
    def add(self, violation):
        raise NotImplementedError

    def get_by_id(self, violation_id):
        raise NotImplementedError

    def update(self, violation):
        raise NotImplementedError

    def delete(self, violation):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def get_by_vehicle_id(self, vehicle_id):
        raise NotImplementedError
