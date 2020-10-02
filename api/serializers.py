from rest_framework import serializers
from api.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ['id']


class CarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ['id']
