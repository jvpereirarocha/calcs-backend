from application.requests.person import CreatePerson
from application.requests.user import CreateUser
from application.services.person_service import CreatePersonService
from application.services.user_service import CreateUserService
from calculations.domain.entities.person import Person
from calculations.domain.entities.user import User

from tests.mocks.mocks_repository.mock_fake_profile_repo import FakeProfileRepo


def test_validate_flow_register_profile(
    mock_person_generate,
    mock_user,
):
    user: User = mock_user
    person: Person = mock_person_generate(user_id=user.user_id)

    user_requester = CreateUser(
        user_id=user.user_id, email=user.email, password=user.password, avatar=None
    )
    person_requester = CreatePerson(
        person_id=person.person_id,
        first_name=person.first_name,
        last_name=person.last_name,
        date_of_birth=person.date_of_birth,
        user_id=user.user_id,
    )

    data = set()
    repo = FakeProfileRepo(data=data)

    assert repo.get_all_users() == set()

    user_service = CreateUserService(requester=user_requester, repo=repo)
    user_service.create_or_update()

    person_service = CreatePersonService(requester=person_requester, repo=repo)
    person_service.create_or_update()

    # not commited yet
    assert repo.get_all_users() == set()
    assert repo.get_first_person() is None
    repo.commit()
    # now commited
    assert len(repo.get_all_users())
    assert repo.get_first_person() is not None
