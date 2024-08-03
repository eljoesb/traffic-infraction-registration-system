class PersonRepository:
    def add(self, person):
        raise NotImplementedError

    def get_by_id(self, person_id):
        raise NotImplementedError

    def get_by_email(self, email):
        raise NotImplementedError

    def update(self, person):
        raise NotImplementedError

    def delete(self, person):
        raise NotImplementedError
