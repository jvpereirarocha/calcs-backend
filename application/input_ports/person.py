from datetime import date
from calculations.domain.abstractions.port.abstract_port import AbstractInputPort
from dataclasses import dataclass

from libs.types.identifiers import PersonUUID


@dataclass
class CreatePerson(AbstractInputPort):
    person_id: PersonUUID
    first_name: str
    last_name: str
    date_of_birth: str | date

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
            self.date_of_birth = date.strptime(self.date_of_birth, "%d/%m/-%Y")
        except ValueError:
            raise ValueError("Date of birth must be in the format DD/MM/YYYY.")
        
    def validate_request(self):
        self._validate_first_name()
        self._validate_last_name()
        self._validate_date_of_birth()
        self._convert_date_of_birth()
