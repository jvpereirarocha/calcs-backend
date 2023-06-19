from typing import Union
from uuid import UUID, uuid4


class BaseUUID(UUID):
    def __init__(self, value: Union[UUID, str, "BaseUUID"] = "") -> None:
        if value == "":
            _id = str(uuid4())
        elif isinstance(value, (UUID, str)) or issubclass(self.__class__, BaseUUID):
            _id = str(value)
        else:
            raise ValueError("Invalid value type to use as UUID")

        super().__init__(_id)


class ExpenseUUID(BaseUUID):
    pass


class RevenueUUID(BaseUUID):
    pass


class BalanceUUID(BaseUUID):
    pass


class AccountUUID(BaseUUID):
    pass


class PersonUUID(BaseUUID):
    pass


class UserUUID(BaseUUID):
    pass
