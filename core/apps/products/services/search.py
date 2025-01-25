from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass

from core.apps.common.clients.elasticsearch import ElasticClient
from core.apps.products.entities.products import ProductEntity


@dataclass
class BaseProductSearchService(ABC):
    
    @abstractmethod
    def upsert_product(self, product: ProductEntity):
        ...
        
    
@dataclass
class ElasticProductSearchService(BaseProductSearchService):
    client: ElasticClient
    index_name: str
    
    @staticmethod
    def _build_as_document(product: ProductEntity) -> dict:
        return {
            'id': product.id,
            'title': product.title,
            'description': product.description,
            'tags': product.tags,
        }
    
    def upsert_product(self, product: ProductEntity):
        self.client.upsert_index(
            index=self.index_name,
            document_id=product.id,
            document=self._build_as_document(product=product),
        )