from abc import ABC, abstractmethod
import random
from core.apps.customers.entities import CustomerEntity
from django.core.cache import cache
from core.apps.customers.exceptions.code import CodeNotFoundException, CodeNotEqualException



class BaseCodeService(ABC):

    @abstractmethod
    def generate_code(self, customer: CustomerEntity) -> str:
        ...

    @abstractmethod
    def validate_code(self, code: str, customer: CustomerEntity) -> None:
        ...


class DjangoCacheCodeService(BaseCodeService):

    def generate_code(self, customer: CustomerEntity) -> str:
        code: str = str(random.randint(100000, 999999))
        cache.set(key=customer.phone, value=code)
        return code

    def validate_code(self, code: str, customer: CustomerEntity) -> None:
        cache_code: str = cache.get(key=customer.phone)

        if code is None:
            raise CodeNotFoundException(code=code)
        
        if cache_code != code:
            raise CodeNotEqualException(
                code=code,
                cache_code=cache_code,
                customer_phone=customer.phone,
            )
        
        cache.delete(key=customer.phone)
