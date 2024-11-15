from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.messages import constants as messages
from django.shortcuts import render
from .models import Car

# Signal to show when a car is added or updated
@receiver(post_save, sender=Car)
def car_added_or_updated(sender, instance, created, **kwargs):
    if created:
        message = f"Car '{instance.name}' has been added successfully!"
    else:
        message = f"Car '{instance.name}' has been updated successfully!"
    
    # Display the message wherever needed (for now, we're just printing it to the console)
    print(message)  # Or use Django's messages framework to display on the frontend
    # You can also use Django's messaging system to show messages to the user
    # messages.success(request, message)

# Signal to show when a car is deleted
@receiver(post_delete, sender=Car)
def car_deleted(sender, instance, **kwargs):
    message = f"Car '{instance.name}' has been deleted successfully!"
    # You can display the message wherever needed, like through messages
    print(message)
    # messages.success(request, message)
