from django.db import models
from django.contrib.auth.models import User


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

    def __str__(self):
        return self.user.username
