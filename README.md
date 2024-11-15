# SellMyCar.com

**SellMyCar.com** is a web-based platform where users can easily list their cars for sale, browse available car listings, and manage their profiles. Built using Django and Bootstrap, this project is designed to make the process of selling and buying cars as simple and intuitive as possible.

## Features

- **Home Page**: Browse a list of available cars for sale.
- **User Profiles**: Users can create and manage their profiles.
- **Post a Car**: Users can list their cars for sale with details like price, model, year, etc.
- **Login/Logout**: Secure user authentication.
- **Sidebar Navigation**: Easy access to different sections such as Home, About Us, and Profile.
- **Responsive Design**: The platform is mobile-friendly and responsive.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite (for local development, can be replaced with PostgreSQL or MySQL)
- **Authentication**: Django's built-in authentication system

## Installation

To run the project locally, follow these steps:


```bash
git clone https://github.com/Sonusrj/SellMyCar.com.git
cd car_sales
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

