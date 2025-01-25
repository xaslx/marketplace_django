from django.http import HttpRequest
from ninja import Query, Router
from punq import Container

from core.api.filters import PaginationIn, PaginationOut
from core.api.schemas import ApiResponse, ListPaginationResponse
from core.api.v1.products.filters import ProductFilters
from core.apps.products.filters.products import ProductFilters as ProductFilterEntity
from core.api.v1.products.schemas import ProductSchema
from core.apps.products.entities.products import ProductEntity
from core.apps.products.services.products import BaseProductService
from core.project.containers import get_container


router: Router = Router(
    tags=['Products'],
)


@router.get(
        '',
        response=ApiResponse[ListPaginationResponse[ProductSchema]],
)
def get_product_list_handler(
    request: HttpRequest,
    filters: Query[ProductFilters],
    pagination_in: Query[PaginationIn],

):
    container: Container = get_container()
    product_service: BaseProductService = container.resolve(BaseProductService)
    
    product_list: list[ProductEntity] = product_service.get_product_list(
                filters=ProductFilterEntity(search=filters.search),
                pagination=pagination_in,
    )
    product_count: int = product_service.get_product_count(
        filters=ProductFilterEntity(search=filters.search)
    )
    pagination_out: PaginationOut = PaginationOut(
            offset=pagination_in.offset,
            limit=pagination_in.limit,
            total=product_count,
    )
    items = [ProductSchema.from_entity(entity=obj) for obj in product_list]
    
    return ApiResponse(data=ListPaginationResponse(
        items=items,
        pagination=pagination_out,
        ),
    )


@router.get('{product_id}', response=ProductSchema)
def get_product_by_id(request: HttpRequest, product_id: int):
    container: Container = get_container()
    product_service: BaseProductService = container.resolve(BaseProductService)
    
    product: ProductEntity = product_service.get_product_by_id(product_id=product_id)
    
    return ProductSchema.from_entity(entity=product)