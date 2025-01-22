from abc import ABC, abstractmethod
from core.apps.customers.entities import CustomerEntity


class BaseSenderService(ABC):

    @abstractmethod
    def send_code(self, customer: CustomerEntity, code: str) -> None:
        ...


class ConsoleSenderService(BaseSenderService):

    def send_code(self, customer: CustomerEntity, code: str) -> None:
        print(f'Code to user: {customer.phone}, sent: {code}')