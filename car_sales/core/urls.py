from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('add_car/', views.add_car, name='add_car'),  # Add car page
    path('register/', views.register, name='register'),
    path('edit_car/<int:car_id>/', views.edit_car, name='edit_car'),  # Edit car
    path('delete_car/<int:car_id>/', views.delete_car, name='delete_car'),  # Delete car
    path('buy/<int:car_id>/', views.buy_car, name='buy_car'),
]
