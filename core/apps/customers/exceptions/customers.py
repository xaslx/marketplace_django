from core.apps.common.exceptions import ServiceException
from dataclasses import dataclass


@dataclass(eq=False)
class CustomerTokenInvalidException(ServiceException):
    token: str
    
    @property
    def message(self):
        return f'A customer with provided token not found'