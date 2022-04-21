from uuid import UUID, uuid4


class BaseUUID:
    def __init__(self) -> None:
        self.id = uuid4().hex

class ExpenseUUID(BaseUUID):
    def __init__(self) -> None:
        super().__init__()

class RevenueUUID(BaseUUID):
    def __init__(self) -> None:
        super().__init__()

class BalanceUUID(BaseUUID):
    def __init__(self) -> None:
        super().__init__()

class AccountUUID(BaseUUID):
    def __init__(self) -> None:
        super().__init__()

class PersonUUID(BaseUUID):
    def __init__(self) -> None:
        super().__init__()