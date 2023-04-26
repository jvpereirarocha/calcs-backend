from datetime import datetime


class AbstractInputPort:
    def __init__(self, created_at: datetime = datetime.now()) -> None:
        self.created_at = created_at