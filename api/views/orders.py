from rest_framework import viewsets
from rest_framework.response import Response
from api.models import Order, Car
from api.serializers import OrderSerializer

#########################################
# LOCATIONS VIEW (Countries & Cities)
########################################


class OrderViewSet(viewsets.ViewSet):
    """
    GET (ALL)
    """

    def list(self):
        orders_db = Order.objects.all()
        orders_serializer = OrderSerializer(orders_db, many=True)

        return Response(orders_serializer)
