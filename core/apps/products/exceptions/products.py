from core.apps.common.exceptions import ServiceException
from dataclasses import dataclass


@dataclass(eq=False)
class ProductNotFoundException(ServiceException):
    product_id: int
    
    @property
    def message(self):
        return f'Product not found'