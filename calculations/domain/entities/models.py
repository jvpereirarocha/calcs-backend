from dataclasses import dataclass
from datetime import datetime


@dataclass
class InheritedModel:
    created_when: datetime = datetime.now()
    modified_when: datetime = datetime.now()
