from rest_framework import serializers
from api.models import Car, Country, City, Model, Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name']


class ModelSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False, read_only=True)

    class Meta:
        model = Model
        fields = ['name', 'brand', 'photo']


class CarSerializer(serializers.ModelSerializer):

    model = ModelSerializer(many=False, read_only=True)

    class Meta:
        model = Car
        fields = ['color_type', 'doors', 'passengers',
                  'fuel_type', 'category', 'model']


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        exclude = ['id']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
