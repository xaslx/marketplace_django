from core.apps.common.exceptions import ServiceException
from dataclasses import dataclass


@dataclass(eq=False)
class CodeException(ServiceException):
    
    @property
    def message(self):
        return f'Auth code exception occured'


@dataclass(eq=False)
class CodeNotFoundException(CodeException):
    code: str

    @property
    def message(self):
        return f'Code not found'
    

@dataclass(eq=False)
class CodeNotEqualException(CodeException):
    code: str
    cache_code: str
    customer_phone: str

    @property
    def message(self):
        return f'Code are not equal'