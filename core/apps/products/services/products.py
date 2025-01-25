from abc import ABC, abstractmethod
from typing import Iterable

from django.db.models import Q
from core.apps.products.exceptions.products import ProductNotFoundException
from core.apps.products.filters.products import ProductFilters
from core.api.filters import PaginationIn
from core.apps.products.entities.products import ProductEntity
from core.apps.products.models.products import Product as ProductModel


class BaseProductService(ABC):
    @abstractmethod
    def get_product_list(
            self,
            filters: ProductFilters,
            pagination: PaginationIn,
    ) -> Iterable[ProductEntity]:
        ...

    @abstractmethod
    def get_product_count(self, filters: ProductFilters) -> int:
        ...

    @abstractmethod
    def get_product_by_id(self, product_id: int) -> ProductEntity:
        ...
        
    @abstractmethod
    def get_all_products(self) -> Iterable[ProductEntity]:
        ...


class ORMProductService(BaseProductService):
    def _build_product_query(self, filters: ProductFilters) -> Q:
        query: Q = Q(is_visible=True)

        if filters.search is not None:
            query &= (Q(title__icontains=filters.search) | Q(description__icontains=filters.search))
        return query

    def get_product_list(
            self,
            filters: ProductFilters,
            pagination: PaginationIn,
    ) -> Iterable[ProductEntity]:
        query: Q  = self._build_product_query(filters=filters)

        qs: Iterable[ProductModel] = ProductModel.objects.filter(query)[
            pagination.offset:pagination.offset + pagination.limit
        ]
        return [product.to_entity() for product in qs]

    def get_product_count(self, filters: ProductFilters) -> int:
        query: Q = self._build_product_query(filters=filters)
        return ProductModel.objects.filter(query).count()

    def get_product_by_id(self, product_id: int) -> ProductEntity | None:
        try:
            product_dto: ProductModel | None = ProductModel.objects.get(pk=product_id)
        except ProductModel.DoesNotExist:
            raise ProductNotFoundException(product_id=product_id)
        
        return product_dto.to_entity()

    def get_all_products(self) -> Iterable[ProductEntity]:
        
        query: Q = self._build_product_query(ProductFilters())
        qs: Iterable[ProductModel] = ProductModel.objects.filter(query)
        
        return [product.to_entity() for product in qs]
            