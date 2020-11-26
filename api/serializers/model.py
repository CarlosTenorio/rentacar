from rest_framework import serializers
from api.models import Model
from .brand import BrandSerializer


class ModelSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False, read_only=True)

    class Meta:
        model = Model
        fields = ['name', 'brand', 'photo']
