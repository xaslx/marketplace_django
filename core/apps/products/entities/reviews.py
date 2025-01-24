from dataclasses import dataclass, field
from datetime import datetime
from core.apps.common.enums import EntityStatus
from core.apps.products.entities.products import ProductEntity
from core.apps.customers.entities import CustomerEntity


@dataclass
class ReviewEntity:
    id: int | None = field(default=None, kw_only=True)
    customer: CustomerEntity | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    product: ProductEntity | EntityStatus = field(default=EntityStatus.NOT_LOADED)
    text: str = field(default='')
    rating: int = field(default=1)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime | None = field(default=None)