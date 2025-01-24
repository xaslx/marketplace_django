from core.apps.common.exceptions import ServiceException
from dataclasses import dataclass


@dataclass(eq=False)
class ReviewInvalidRatingExcpetion(ServiceException):
    raing: int
    
    @property
    def message(self):
        return f'Rating is not valid'