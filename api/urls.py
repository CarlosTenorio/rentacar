from django.urls import path
from api import views


car_list = views.CarViewSet.as_view({'get': 'list', 'post': 'create'})
car_detail = views.CarViewSet.as_view(
    {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})
locations_list = views.LocationViewSet.as_view({'get': 'list'})
order_list = views.OrderViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('cars/', car_list, name='card-list'),
    path('cars/<int:car_id>/', car_detail, name='card-detail'),
    path('locations/', locations_list, name='locations-list'),
    path('orders/', locations_list, name='orders-list'),
]
