from django.db import models
from .car import Car
from .extend_user import ExtendUser


class Order(models.Model):
    date_signed = models.DateTimeField(auto_now_add=True,
                                       null=False, blank=False, verbose_name='When the order was made')
    date_start = models.DateTimeField(
        null=False, blank=False, verbose_name='Start date')
    date_end = models.DateTimeField(
        null=False, blank=False, verbose_name='End date')

    car = models.ForeignKey(Car, on_delete=models.PROTECT,
                            related_name="car_order", verbose_name='Car',
                            null=True, blank=False)

    user = models.ForeignKey(ExtendUser, on_delete=models.PROTECT,
                             related_name="user_order", verbose_name='User',
                             null=True, blank=False)

    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False, verbose_name='Creation date')
    updated_at = models.DateTimeField(
        auto_now=True, null=False, blank=False, verbose_name='Update date')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'{self.date_start}-{self.date_end}'
