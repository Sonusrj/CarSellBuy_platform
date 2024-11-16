# 🚗 SellMyCar.com

**SellMyCar.com** is a user-friendly platform for buying and selling cars. With an intuitive design built using Django and Bootstrap, it makes car trading hassle-free! 🛠️

## ✨ Features

- 🏠 **Home Page**: Browse available cars for sale.  
- 👤 **User Profiles**: Create and manage your profile.  
- 🚙 **Post a Car**: List cars for sale with details like price, model, and year.  
- 🔐 **Login/Logout**: Secure authentication for users.  
- 📋 **Sidebar Navigation**: Quick access to sections like Home, About Us, and Profile.    

## 💻 Tech Stack

- **Backend**: Django (Python)  
- **Frontend**: HTML, CSS, Bootstrap 5  
- **Database**: SQLite (default) - switchable to PostgreSQL/MySQL  
- **Authentication**: Django's built-in authentication system  

## 🛠️ Installation

Follow these steps to set up the project locally:  

1. Clone the repository:  
   ```bash
   git clone https://github.com/Sonusrj/SellMyCar.com.git
   cd car_sales
2. Install the dependencies
   ```bash
    pip install -r requirements.txt

4. Apply database migrations
   ```bash
    python manage.py migrate

6. Create a superuser (admin)
   ```bash
    python manage.py createsuperuser

8. Run the development server
   ```bash
    python manage.py runserver

