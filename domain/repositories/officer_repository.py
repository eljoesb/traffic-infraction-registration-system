class OfficerRepository:
    def add(self, officer):
        raise NotImplementedError

    def get_by_id(self, officer_id):
        raise NotImplementedError

    def get_by_unique_id(self, unique_id):
        raise NotImplementedError

    def update(self, officer):
        raise NotImplementedError

    def delete(self, officer):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError
