from rest_framework import viewsets, status
from rest_framework.response import Response
from api.models import Order
from api.serializers import OrderSerializer, OrderCreateSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#########################################
# ORDERS VIEW
########################################


class OrderViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        GET (ALL)
        """
        orders_db = Order.objects.all()
        orders_serializer = OrderSerializer(orders_db, many=True)

        return Response(orders_serializer.data)

    @swagger_auto_schema(request_body=OrderCreateSerializer)
    def create(self, request):
        """
        POST
        """

        order_serializer = OrderCreateSerializer(
            data=request.data, context={'request': request})
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(order_serializer.data, status=status.HTTP_201_CREATED)
        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
