from django.db import models
from .category import Category
from .model import Model
from .city import City

FUEL_TYPE = (
    (0, 'GASOLINE'),
    (1, 'DIESEL')
)
COLOR = (
    (0, 'WHITE'),
    (1, 'RED'),
    (2, 'BLACK'),
    (3, 'BLUE'),
    (4, 'YELLOW'),
    (5, 'GREEN'),
    (6, 'GREY'),
    (7, 'ORANGE')
)


class Car(models.Model):

    color_type = models.IntegerField(null=False, blank=False,
                                     verbose_name='Color', default=0, choices=COLOR)
    doors = models.IntegerField(null=False, blank=False, verbose_name='Doors')
    passengers = models.IntegerField(
        null=False, blank=False, verbose_name='Passengers number')
    registration = models.CharField(max_length=8,
                                    null=False, blank=False, verbose_name='Registration number')
    booking = models.BooleanField(verbose_name='Is already booking')
    fuel_type = models.IntegerField(null=False, blank=False,
                                    verbose_name='Fuel type', default=0, choices=FUEL_TYPE)

    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name="category_car", verbose_name='Category',
                                 null=False, blank=False)

    model = models.ForeignKey(Model, on_delete=models.PROTECT,
                              related_name="model_car", verbose_name='Model',
                              null=False, blank=False)

    city = models.ForeignKey(City, on_delete=models.PROTECT,
                             related_name="city_car", verbose_name='City',
                             null=True, blank=False, default=None)

    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False, verbose_name='Creation date')
    updated_at = models.DateTimeField(
        auto_now=True, null=False, blank=False, verbose_name='Update date')

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return f'{self.id} - {self.model}'
