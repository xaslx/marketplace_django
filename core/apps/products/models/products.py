from django.db import models
from core.apps.common.models import TimedBaseModel






class Product(TimedBaseModel):
    title = models.CharField(
        max_length=255,
        verbose_name='Название товара',
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание товара',
    )
    is_visible = models.BooleanField(
        default=True, 
        verbose_name='Видимость товара в каталоге',
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.title}'




