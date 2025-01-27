from django.db import models
from core.apps.common.models import TimedBaseModel
from core.apps.products.entities.products import ProductEntity as ProductEntity
from django.contrib.postgres.fields import ArrayField


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
    tags = ArrayField(
        verbose_name='Теги товара',
        default=list,
        base_field=models.CharField(max_length=100),
    )

    def to_entity(self) -> ProductEntity:
        return ProductEntity(
            id=self.pk,
            title=self.title,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
            tags=self.tags,
        )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.title}'




