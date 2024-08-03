class VehicleRepository:
    def add(self, vehicle):
        raise NotImplementedError

    def get_by_id(self, vehicle_id):
        raise NotImplementedError

    def get_by_license_plate(self, license_plate):
        raise NotImplementedError

    def update(self, vehicle):
        raise NotImplementedError

    def delete(self, vehicle):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def get_by_person_id(self, person_id):
        raise NotImplementedError
