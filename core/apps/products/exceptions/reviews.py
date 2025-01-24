from core.apps.common.exceptions import ServiceException
from dataclasses import dataclass


@dataclass(eq=False)
class ReviewInvalidRatingExcpetion(ServiceException):
    rating: int
    
    @property
    def message(self):
        return f'Rating is not valid'
    
    
@dataclass(eq=False)
class SingleReviewErrorException(ServiceException):
    product_id: int
    customer_id: int
    
    @property
    def message(self):
        return f'The user already posted a review on this product'