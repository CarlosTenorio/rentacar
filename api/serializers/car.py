from rest_framework import serializers
from api.models import Car
from .model import ModelSerializer
from .category import CategorySerializer


class CarSerializer(serializers.ModelSerializer):

    model = ModelSerializer(many=False, read_only=True)
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Car
        fields = ['color_type', 'doors', 'passengers',
                  'fuel_type', 'category', 'model']
