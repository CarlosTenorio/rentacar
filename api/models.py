from django.db import models
from django.contrib.auth.models import User


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


class Model(models.Model):
    name = models.CharField(max_length=128, null=False,
                            blank=False, verbose_name='Name')
    Year = models.IntegerField(null=False, blank=False, verbose_name='Year')

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


class Car(models.Model):
    FUEL_TYPE = (
        (0, 'GASOLINE'),
        (1, 'DIESEL')
    )

    color = models.CharField(max_length=128, null=False,
                             blank=False, verbose_name='Color')
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

    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False, verbose_name='Creation date')
    updated_at = models.DateTimeField(
        auto_now=True, null=False, blank=False, verbose_name='Update date')

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class Order(models.Model):
    date_signed = models.DateTimeField(
        null=False, blank=False, verbose_name='When the order was made')
    date_start = models.DateTimeField(
        null=False, blank=False, verbose_name='Start date')
    date_end = models.DateTimeField(
        null=False, blank=False, verbose_name='End date')

    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False, verbose_name='Creation date')
    updated_at = models.DateTimeField(
        auto_now=True, null=False, blank=False, verbose_name='Update date')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class ExtendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=15, null=False,
                           blank=False, verbose_name='DNI')
    born_year = models.IntegerField(null=False,
                                    blank=False, verbose_name='Born year')
    is_driver = models.BooleanField(verbose_name='Is driver')

    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False, verbose_name='Creation date')
    updated_at = models.DateTimeField(
        auto_now=True, null=False, blank=False, verbose_name='Update date')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
