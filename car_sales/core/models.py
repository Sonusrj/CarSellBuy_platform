from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


def get_default_user():
    user = User.objects.first()
    return user.id if user else None

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images/') 
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)
    date_added = models.DateTimeField(auto_now_add=True)
    is_bought = models.BooleanField(default=False) 
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='bought_cars')
   
    def __str__(self):
        return f'{self.name} - {self.model}'
    
