from dataclasses import dataclass
from datetime import datetime



@dataclass
class CustomerEntity:
    id: int
    phone: str
    created_at: datetime