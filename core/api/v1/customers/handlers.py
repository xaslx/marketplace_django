from django.http import HttpRequest
from ninja import Router
from ninja.errors import HttpError
from punq import Container

from core.api.schemas import ApiResponse
from core.api.v1.customers.schemas import (AuthInSchema, AuthOutSchema,
                                           TokenInSchema, TokenOutSchema)
from core.apps.common.exceptions import ServiceException
from core.apps.customers.services.auth import BaseAuthService
from core.project.containers import get_container


router: Router = Router(
    tags=['Customers'],
)


@router.post(
        'auth',
        response=ApiResponse[AuthOutSchema],
        operation_id='authorize',
)
def auth_handler(
    request: HttpRequest,
    schema: AuthInSchema,
):
    container: Container = get_container()
    auth_service: BaseAuthService = container.resolve(BaseAuthService)
    
    auth_service.authorize(phone=schema.phone)
    
    return ApiResponse(
        data=AuthOutSchema(
            message=f'Code sent to: {schema.phone}',
        )
    )

    
@router.post(
        'confirm',
        response=ApiResponse[TokenOutSchema],
        operation_id='confirm',
)
def get_token_handler(
    request: HttpRequest,
    schema: TokenInSchema,
):
    container: Container = get_container()
    auth_service: BaseAuthService = container.resolve(BaseAuthService)
    
    try:
        token: str = auth_service.confirm(code=schema.code, phone=schema.phone)
    except ServiceException as exception:
        raise HttpError(
            status_code=400,
            message=exception.message
        )
        
    return ApiResponse(data=TokenOutSchema(token=token))