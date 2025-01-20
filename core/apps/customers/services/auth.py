from abc import ABC, abstractmethod
from dataclasses import dataclass

from core.apps.customers.entities import CustomerEntity
from core.apps.customers.services.codes import BaseCodeService
from core.apps.customers.services.customer import BaseCustomerService
from core.apps.customers.services.sender import BaseSenderService


@dataclass(eq=False)
class BaseAuthService(ABC):
    customer_service: BaseCustomerService
    code_service: BaseCodeService
    sender_service: BaseSenderService

    @abstractmethod
    def authorize(self, phone: str) -> None:
        ...

    @abstractmethod
    def confirm(self, code: str, phone: str) -> str:
        ...


@dataclass
class AuthService(BaseAuthService):
    
    def authorize(self, phone: str) -> None:
        customer: CustomerEntity = self.customer_service.get_or_create(phone=phone)
        code: str = self.code_service.generate_code(customer=customer)
        self.sender_service.send_code(code=code)

    def confirm(self, code: str, phone: str) -> str:
        customer: CustomerEntity = self.customer_service.get(phone=phone)
        self.code_service.validate_code(code=code, customer=customer)
        return self.customer_service.generate_token(customer=customer)