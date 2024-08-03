from domain.repositories.person_repository import PersonRepository
from domain.entities.person import Person

class SQLAlchemyPersonRepository(PersonRepository):
    def __init__(self, session):
        self.session = session

    def add(self, person):
        self.session.add(person)
        self.session.commit()

    def get_by_id(self, person_id):
        return self.session.query(Person).filter_by(id=person_id).first()

    def get_by_email(self, email):
        return self.session.query(Person).filter_by(email=email).first()

    def update(self, person):
        self.session.commit()

    def delete(self, person):
        self.session.delete(person)
        self.session.commit()
