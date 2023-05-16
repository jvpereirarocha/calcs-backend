import json
from typing import Iterable, List, Optional, Union
from calculations.domain.abstractions.parser.abstract_parser import AbstractParser
from calculations.domain.entities.models import BaseModel
from calculations.domain.entities.user import User


class CreatedOrUpdatedUserParser(AbstractParser):
    def to_json(self, data: Optional[User] = None) -> str:
        if data:
            message = f"User {data.user_id} has been updated!"
        else:
            message = f"User has been created!"
        
        return json.dumps(message)


class AllUsersParser(AbstractParser):
    def to_json(self, data: Iterable[User]) -> str:
        list_of_parsed_users = []
        for user in data:
            user_as_dict = user.to_dict()
            list_of_parsed_users.append(
                json.dumps(user_as_dict)
            )
        return list_of_parsed_users