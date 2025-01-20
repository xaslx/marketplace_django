from core.api.filters import PaginationIn
from core.api.v1.products.filters import ProductFilters
from core.apps.products.services.products import BaseProductService
import pytest
from core.apps.products.models.products import Product
from tests.factories.products import ProductModelFactory

@pytest.mark.django_db
def test_products_count_zero(product_service: BaseProductService):
    """Тест с нулевым количеством товаров в базе"""

    res: int = product_service.get_product_count(filters=ProductFilters())
    assert res == 0, f'{res=}'


@pytest.mark.django_db
def test_products_count_not_zero(product_service: BaseProductService):
    """Тест с количеством товаров больше 0"""
    
    expected_count: int = 5
    ProductModelFactory.create_batch(size=expected_count)

    products_count: int = product_service.get_product_count(filters=ProductFilters())
    assert products_count == expected_count, f'{products_count=}'


@pytest.mark.django_db
def test_get_product_list(product_service: BaseProductService):
    """Тест на получение списка продуктов"""

    expected_count: int = 5
    products = ProductModelFactory.create_batch(size=expected_count)
    product_titles = {product.title for product in products}

    fetched_products = product_service.get_product_list(filters=ProductFilters(), pagination=PaginationIn())
    fetched_titles = {product.title for product in fetched_products}

    assert len(fetched_titles) == expected_count, f'{fetched_titles=}'
    assert product_titles == fetched_titles

    
@pytest.mark.skip(reason='not implemented')
def test_product_search():
    assert True