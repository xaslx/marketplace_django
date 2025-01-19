from pytest import fixture
from core.apps.products.services.products import BaseProductService, ORMProductService


@fixture(scope='session')
def product_service() -> BaseProductService:
    return ORMProductService()