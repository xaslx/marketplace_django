from dataclasses import asdict
from logging import Logger
from ninja import Router, Header
from django.http import HttpRequest
import orjson
from core.api.schemas import ApiResponse
from core.api.v1.reviews.schemas import ReviewInSchema, CreateReviewSchema, ReviewOutSchema
from core.apps.common.exceptions import ServiceException
from ninja.errors import HttpError
from punq import Container

from core.apps.products.entities.reviews import ReviewEntity
from core.apps.products.services.reviews import BaseReviewService
from core.apps.products.use_cases.reviews.create import CreateReviewUseCase
from core.project.containers import get_container


router: Router = Router(
    tags=['Отзывы']
)


@router.post(
    '{product_id}/reviews',
    response=ApiResponse[ReviewOutSchema],
    operation_id='createReview',
)
def add_review(
    request: HttpRequest,
    product_id: int,
    schema: ReviewInSchema,
    token: str = Header(alias='Auth-Token'),
):
    container: Container = get_container()
    use_case: CreateReviewUseCase = container.resolve(CreateReviewUseCase)

    try:
        review: ReviewEntity = use_case.execute(
            product_id=product_id,
            customer_token=token,
            review=schema.to_entity(),
    )
    except ServiceException as exception:
        logger: Logger = container.resolve(Logger)
        logger.error(
            msg='User could not create review',
            extra={'error_meta': orjson.dumps(exception).decode()},
        )
        raise HttpError(
            status_code=400,
            message=exception.message,
        )

    return ApiResponse(
        data=ReviewOutSchema.from_entity(review=review)
    )