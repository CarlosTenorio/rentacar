from django.db import models
from .brand import Brand


class Model(models.Model):
    name = models.CharField(max_length=128, null=False,
                            blank=False, verbose_name='Name')
    year = models.IntegerField(null=False, blank=False, verbose_name='Year')

    brand = models.ForeignKey(Brand, on_delete=models.PROTECT,
                              related_name="brand_model", verbose_name='Brand',
                              null=False, blank=False)

    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False, verbose_name='Creation date')
    updated_at = models.DateTimeField(
        auto_now=True, null=False, blank=False, verbose_name='Update date')

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'

    def __str__(self):
        return self.name
