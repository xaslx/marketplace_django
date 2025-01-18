from pydantic import BaseModel
from datetime import datetime

from core.apps.products.entities.products import Product




class ProductSchema(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime
    updated_at: datetime | None = None

    @staticmethod
    def from_entity(entity: Product) -> 'ProductSchema':
        return ProductSchema(
            id=entity.id,
            title=entity.title,
            description=entity.description,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )