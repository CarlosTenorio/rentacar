from rest_framework import serializers
from api.models import Car


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ['id']
