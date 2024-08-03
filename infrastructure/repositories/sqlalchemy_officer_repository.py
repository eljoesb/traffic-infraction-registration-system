from domain.repositories.officer_repository import OfficerRepository
from domain.entities.officer import Officer

class SQLAlchemyOfficerRepository(OfficerRepository):
    def __init__(self, session):
        self.session = session

    def add(self, officer):
        self.session.add(officer)
        self.session.commit()

    def get_by_id(self, officer_id):
        return self.session.query(Officer).filter_by(id=officer_id).first()

    def get_by_unique_id(self, unique_id):
        return self.session.query(Officer).filter_by(unique_id=unique_id).first()

    def update(self, officer):
        self.session.commit()

    def delete(self, officer):
        self.session.delete(officer)
        self.session.commit()

    def get_all(self):
        return self.session.query(Officer).all()
