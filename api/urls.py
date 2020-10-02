from django.urls import path
from api import views


car_list = views.CarViewSet.as_view({'get': 'list', 'post': 'create'})
car_detail = views.CarViewSet.as_view({'get': 'retrieve', 'put': 'update'})

urlpatterns = [
    path('cars/', car_list, name='card-list'),
    path('cars/<int:id>/', car_detail, name='card-detail'),
]