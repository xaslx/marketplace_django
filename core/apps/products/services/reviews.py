from abc import ABC, abstractmethod
from core.apps.customers.entities import CustomerEntity
from core.apps.products.entities.products import ProductEntity
from core.apps.products.entities.reviews import ReviewEntity
from core.apps.products.exceptions.reviews import ReviewInvalidRatingExcpetion
from dataclasses import dataclass

from core.apps.products.models.reviews import Review


class BaseReviewService(ABC):
    
    @abstractmethod
    def save_review(
        self, 
        product: ProductEntity,
        customer: CustomerEntity,
        review: ReviewEntity,
    ) -> ReviewEntity:
        ...
        

class ORMReviewService(BaseReviewService):
    
    def save_review(
        self, 
        product: ProductEntity,
        customer: CustomerEntity,
        review: ReviewEntity,
    ) -> ReviewEntity:
        review_dto: Review = Review.from_entity(review=review, product=product, customer=customer)
        review_dto.save()
        return review_dto.to_entity()
        


class BaseReviewValidatorService(ABC):
    
    @abstractmethod
    def validate(
        self,
        review: ReviewEntity,
        customer: CustomerEntity | None = None,
        product: ProductEntity | None = None,
    ) -> None: 
        ...
        
        
class ReviewRatingValidatorService(BaseReviewValidatorService):
    
    def validate(
        self,
        review: ReviewEntity,
        *args,
        **kwargs,
    ) -> None: 
        if not (1 <= review.rating <= 5):
            raise ReviewInvalidRatingExcpetion(rating=review.rating)
        

@dataclass
class ComposedReviewValidatorService(BaseReviewValidatorService):
    validators: list[BaseReviewValidatorService]
    
    def validate(
        self,
        review: ReviewEntity,
        customer: CustomerEntity | None = None,
        product: ProductEntity | None = None,
    ) -> None:
        for validator in self.validators:
            validator.validate(review=review, customer=customer, product=product)