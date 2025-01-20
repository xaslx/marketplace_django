from uuid import uuid4
from django.db import models
from core.apps.common.models import TimedBaseModel
from core.apps.customers.entities import CustomerEntity



class Customer(TimedBaseModel):
    phone = models.CharField(
        verbose_name='Номер телефона',
        max_length=11,
        default=uuid4,
        unique=True,
    )
    token = models.CharField(
        verbose_name='Токен аутентификации',
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return self.phone

    def to_entity(self) -> CustomerEntity:
        return CustomerEntity(
            id=self.pk,
            phone=self.phone,
            created_at=self.created_at,
        )

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
