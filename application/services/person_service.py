from application.requests.person import CreatePerson
from calculations.domain.abstractions.repository.profiles.abstract_repo_profile import (
    AbstractProfileRepo,
)
from calculations.domain.abstractions.services.abstract_service import (
    AbstractCreateOrUpdateService,
)
from calculations.domain.entities.person import Person


class CreatePersonService(AbstractCreateOrUpdateService):
    def __init__(self, requester: CreatePerson, repo: AbstractProfileRepo):
        self.requester = requester
        self.repo = repo

    def _create_new_or_update_person(self):
        person_already_exists = self.repo.get_person_by_id(
            person_id=self.requester.person_id
        )
        if person_already_exists:
            person_already_exists.update_person(
                first_name=self.requester.first_name,
                last_name=self.requester.last_name,
                date_of_birth=self.requester.date_of_birth,
            )
            self.repo.save_person(person=person_already_exists)
            return person_already_exists

        person = Person.create_person(
            person_id=self.requester.person_id,
            first_name=self.requester.first_name,
            last_name=self.requester.last_name,
            date_of_birth=self.requester.date_of_birth,
            user_id=self.requester.user_id,
        )
        self.repo.save_person(person=person)
        return person

    def create_or_update(self):
        return self._create_new_or_update_person()
