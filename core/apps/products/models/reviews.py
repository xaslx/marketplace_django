from core.apps.common.models import TimedBaseModel
from django.db import models


class ProductReview(TimedBaseModel):
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
    
    def __str__(self):
        return f'{self.product}'
    
    class Meta:
        verbose_name = 'Отзывы товара'
        verbose_name_plural = 'Отзывы товаров'
        unique_together = (
            ('customer', 'product'),
        )