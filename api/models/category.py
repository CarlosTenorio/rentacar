from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, null=False,
                            blank=False, verbose_name='Name')
    price = models.FloatField(null=False, blank=False, verbose_name='Price')

    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False, verbose_name='Creation date')
    updated_at = models.DateTimeField(
        auto_now=True, null=False, blank=False, verbose_name='Update date')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
