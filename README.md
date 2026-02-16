# Room Reservation System

## Project description
Web application for managing company meeting rooms.
Employees can check room availability and create reservations.

## Features
- user login/logout
- list of rooms
- room details
- create reservation
- edit reservation
- cancel reservation
- user reservation list
- conflict validation
- admin panel for rooms and reservations

## Requirements
- Python 3.12+
- Django
- virtualenv

## Installation

- Clone repository: git clone <repo_url>cd rejestracja_sal
- Create virtual environment: python -m venv venv
venv\Scripts\activate
- Install dependencies: pip install django crispy-bootstrap5 django-crispy-forms
- Apply migrations: python manage.py migrate
- Create admin user: python manage.py createsuperuser
- Run server: python manage.py runserver

Open browser: http://127.0.0.1:8000


## Usage
1. Login as user
2. Browse rooms
3. Create reservation
4. Manage your reservations

Administrator can manage rooms and reservations via `/admin`