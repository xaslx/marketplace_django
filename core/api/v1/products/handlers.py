from ninja import Query, Router
from django.http import HttpRequest
from core.api.filters import PaginationIn, PaginationOut
from core.api.v1.products.filters import ProductFilters
from core.api.v1.products.schemas import ProductSchema
from core.apps.products.entities.products import Product
from core.apps.products.services.products import BaseProductService, ORMProductService
from core.api.schemas import ApiResponse, ListPaginationResponse

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
    service: BaseProductService = ORMProductService()
    product_list: list[Product] = service.get_product_list(filters=filters, pagination=pagination_in)
    product_count: int = service.get_product_count(filters=filters)
    pagination_out: PaginationOut = PaginationOut(
            offset=pagination_in.offset, 
            limit=pagination_in.limit,
            total=product_count,
    )
    items = [ProductSchema.from_entity(entity=obj) for obj in product_list]
    return ApiResponse(data=ListPaginationResponse(items=items, pagination=pagination_out))



@router.get('{product_id}', response=ProductSchema)
def get_product_by_id(request: HttpRequest, product_id: int):
    service: BaseProductService = ORMProductService()
    product: Product = service.get_product_by_id(id=product_id)
    return ProductSchema.from_entity(entity=product)