from abc import ABC, abstractmethod
from uuid import uuid4

from core.apps.customers.entities import CustomerEntity
from core.apps.customers.exceptions.customers import CustomerTokenInvalidException
from core.apps.customers.models import Customer


class BaseCustomerService(ABC):

    @abstractmethod
    def get_or_create(self, phone: str) -> CustomerEntity:
        ...

    @abstractmethod
    def generate_token(self, customer: CustomerEntity) -> str:
        ...

    @abstractmethod
    def get(self, phone: str) -> CustomerEntity:
        ...
    
    @abstractmethod
    def get_by_token(self, token: str) -> CustomerEntity | None:
        ...


class ORMCustomerService(BaseCustomerService):

    def get_or_create(self, phone: str) -> CustomerEntity:
        customer_dto: Customer
        customer_dto, _ = Customer.objects.get_or_create(phone=phone)
        return customer_dto.to_entity()
    
    def get(self, phone: str) -> CustomerEntity:
        customer_dto: Customer = Customer.objects.get(phone=phone)
        return customer_dto.to_entity()
    
    def generate_token(self, customer: CustomerEntity) -> str:
        new_token: str = str(uuid4())
        Customer.objects.filter(phone=customer.phone).update(
            token=new_token,
        )
        return new_token
    
    def get_by_token(self, token: str) -> CustomerEntity | None:
        try:
            customer_dto: Customer = Customer.objects.get(token=token)
        except Customer.DoesNotExist:
            raise CustomerTokenInvalidException(token=token)
        
        return customer_dto.to_entity()