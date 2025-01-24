from core.apps.common.models import TimedBaseModel
from django.db import models

from core.apps.customers.entities import CustomerEntity
from core.apps.products.entities.products import ProductEntity
from core.apps.products.entities.reviews import ReviewEntity


class Review(TimedBaseModel):
    customer = models.ForeignKey(
        to='customers.Customer',
        verbose_name='Пользователь',
        related_name='product_reviews',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        to='products.Product',
        verbose_name='Товар',
        related_name='product_reviews',
        on_delete=models.CASCADE,
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг пользователя',
        default=1,
    )
    text = models.TextField(
        verbose_name='Текст отзыва',
        blank=True,
        default='',
    )
    
    @classmethod
    def from_entity(
        cls,
        review: ReviewEntity,
        product: ProductEntity,
        customer: CustomerEntity,
    ) -> 'Review':
        return cls(
            pk=review.id,
            product_id=product.id,
            customer_id=customer.id,
            text=review.text,
            rating=review.rating,
        )

    def to_entity(self) -> ReviewEntity:
        return ReviewEntity(
            text=self.text,
            rating=self.rating,
            id=self.id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
    
    def __str__(self):
        return f'{self.product}'
    
    class Meta:
        verbose_name = 'Отзывы товара'
        verbose_name_plural = 'Отзывы товаров'
        unique_together = (
            ('customer', 'product'),
        )