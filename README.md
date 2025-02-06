# Restaurant Kitchen Service

## Description
A Django-based application that streamlines kitchen service management, 
allowing users to track dishes, dish types, cooks and ingredients.
The system is designed to help kitchen services keep their work organized with features for managing dishes,
assigning cooks, and logging information about dishes and dish types.
## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Technologies Used](#Technologies-Used)
- [Demo](#Demo)


## Features
- Manage your dish types and track which and how many meals belong to them.
- Assign cooks to dishes and track their experience.
- Record information about dishes, including type, recipe, and status (whether someone is responsible for preparing it or not).
- Built-in search by dish name, dish type name, username and ingredient name.
- Responsive design using Soft UI Design Django and Bootstrap 5.

## Installation
To set up this project, you need to have Python3 already installed. Then, run these commands:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/restaurant-kitchen-service
   cd restaurant-kitchen-service
2. Create a virtual environment:
   ```bash
   python -m venv venv
3. Activate the virtual environment:
   ```bash
   venv\Scripts\activate # On Window
   source venv/bin/activate # On macOS/Linux
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
5. Set up the database:
   ```bash
   python manage.py migrate
6. Run the Django development server:
   ```bash
   python manage.py runserver

## Technologies Used
- Django
- Python
- PostgreSQL
- Soft UI Design Django
- Bootstrap 5

## Demo
Sign in to test functionality.
````
Login: test_user

Password: Login_test123
````
![Project Demo](https://github.com/onyevyerov/restaurant-kitchen-service/blob/develop/images/demo.png?raw=true)