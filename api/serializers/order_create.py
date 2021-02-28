from rest_framework import serializers
from api.models import Order


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['id', 'user', 'created_at', 'updated_at']
