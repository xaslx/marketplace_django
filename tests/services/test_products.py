from core.api.v1.products.filters import ProductFilters
from core.apps.products.services.products import BaseProductService
import pytest
from core.apps.products.models.products import Product

@pytest.mark.django_db
def test_products_count_zero(product_service: BaseProductService):
    """Тест с нулевым количеством товаров в базе"""

    res: int = product_service.get_product_count(filters=ProductFilters())
    assert res == 0, f'{res=}'


@pytest.mark.django_db
def test_products_count_not_zero(product_service: BaseProductService):
    """Тест с количеством товаров больше 0"""

    Product.objects.create()



@pytest.mark.skip(reason='not implemented')
def test_product_search():
    assert True