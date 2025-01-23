from dataclasses import dataclass, field
from core.apps.common.enums import EntityStatus
from core.apps.products.entities.products import ProductEntity
from core.apps.customers.entities import CustomerEntity


@dataclass
class ReviewEntity:
    customer: CustomerEntity | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    product: ProductEntity | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    text: str = field(default='')
    rating: int = field(default=1)