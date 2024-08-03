class GenerateReport:
    def __init__(self, person_repository):
        self.person_repository = person_repository

    def execute(self, email):
        person = self.person_repository.get_by_email(email)
        if not person:
            raise ValueError("Person not found")
        return person.vehicles
