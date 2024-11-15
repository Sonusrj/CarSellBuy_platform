from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required 
from .forms import CarForm, RegisterForm
from django.contrib.auth.views import LogoutView
from .models import Car
from django.contrib import messages
# View to handle the home page
def home(request):
    cars = Car.objects.all()  
    return render(request, 'home.html', {'cars': cars})

@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)  
        if form.is_valid():
            car = form.save(commit=False)  
            car.user = request.user  # Link the car to the current user
            car.save()

            # Add success message after car is added
            messages.success(request, f"Car '{car.name}' has been added successfully!")

            return redirect('home')  
    else:
        form = CarForm()

    return render(request, 'add_car.html', {'form': form})

@login_required
def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if car.user != request.user:  
        return redirect('home')

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CarForm(instance=car)

    return render(request, 'edit_car.html', {'form': form, 'car': car})

@login_required
def buy_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')

        car.is_bought = True
        car.buyer = request.user  # Set buyer to the current user
        car.save()
        
        # Send the email with purchase details
        send_mail(
            'Purchase Confirmation - SellMyCar.com',
            f'You have successfully purchased the car: {car.name}\nPrice: ${car.price}\nPayment Method: {payment_method}',
            settings.DEFAULT_FROM_EMAIL,
            [request.user.email],  # Send to logged-in user's email
            fail_silently=False,
        )
        
        messages.success(request, f'You have successfully purchased the car: {car.name}.')

        
        return redirect('profile')  

    return render(request, 'buy_car.html', {'car': car})

@login_required
def profile(request):
    user = request.user
    added_cars = Car.objects.filter(user=user)  # Cars added by the user
    bought_cars = Car.objects.filter(buyer=user)  # Cars bought by the user
    return render(request, 'profile.html', {
        'user': user,
        'added_cars': added_cars,
        'bought_cars': bought_cars
    })

@login_required
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if car.user != request.user: 
        return redirect('home') 

    if request.method == 'POST':
        
        car.delete()  
        messages.success(request, f"Car '{car.name}' has been deleted successfully!")
        return redirect('home')

    return render(request, 'delete_car.html', {'car': car})
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            return redirect('home')  
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})

def about_us(request):
    return render(request, 'about_us.html')

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return redirect('login') 