from datetime import date, datetime
from calculations.domain.abstractions.port.abstract_port import AbstractInputPort
from dataclasses import dataclass

from libs.types.identifiers import PersonUUID, UserUUID


@dataclass
class CreatePerson(AbstractInputPort):
    person_id: PersonUUID
    first_name: str
    last_name: str
    date_of_birth: str | date
    user_id: str

    _valid_request: bool = False

    def _validate_first_name(self):
        if not self.first_name:
            raise ValueError("First name is required.")
        
    def _validate_last_name(self):
        if not self.last_name:
            raise ValueError("Last name is required.")
        
    def _validate_date_of_birth(self):
        if not self.date_of_birth:
            raise ValueError("Date of birth is required.")
        
    def _convert_date_of_birth(self):
        try:
            converted_date = datetime.strptime(self.date_of_birth, "%d/%m/%Y")
            self.date_of_birth = converted_date.date()
        except ValueError:
            raise ValueError("Date of birth must be in the format DD/MM/YYYY.")
        
    def _convert_str_to_uuid(self):
        try:
            self.person_id = UserUUID(self.user_id)
        except ValueError:
            raise ValueError("User ID must be a valid UUID.")
        
    def validate_request(self):
        self._validate_first_name()
        self._validate_last_name()
        self._validate_date_of_birth()
        self._convert_date_of_birth()
        self._convert_str_to_uuid()
        self._valid_request = True

    def request_is_valid(self):
        return self._valid_request
