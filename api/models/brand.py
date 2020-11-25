from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=128, null=False,
                            blank=False, verbose_name='Name')

    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False, verbose_name='Creation date')
    updated_at = models.DateTimeField(
        auto_now=True, null=False, blank=False, verbose_name='Update date')

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name
