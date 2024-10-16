# Task Management System API

This project is a Task Management API built with Django and Django REST Framework, featuring JWT authentication. The API allows users to create, read, update, and delete tasks (CRUD) with additional functionality for filtering and sorting tasks. Only authenticated users can perform CRUD operations on tasks.

## Features

- **User Registration and Login**: Users can register and log in using JWT-based authentication.
- **CRUD Operations**: Authenticated users can create, view, update, and delete tasks.
- **Task Model**:
  - Title (string, required)
  - Description (optional)
  - Status (choices: pending, in-progress, completed)
  - Priority (choices: low, medium, high)
  - Due Date (cannot be a past date)
- **Logical Status Flow**: Status must follow the logical flow from `pending` → `in-progress` → `completed`.
- **Restrictions**: Once a task is marked as `completed`, it cannot be updated.
- **Filtering**: Tasks can be filtered by `status` and `priority`.
- **Sorting**: Tasks can be sorted by `due date` or `priority`.

## Requirements

- Python 3.x
- Django 4.x
- Django REST Framework
- django-filter
- djangorestframework-simplejwt

## Installation

1. **Clone the repository**:
   git clone https://github.com/your-username/task-management-system.git
   cd task-management-system

## Create and activate a virtual environment:
  python -m venv venv
  source venv/bin/activate

## Create SuperUSer:
  python manage.py createsuperuser

## Run Migrations and development server:
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver

## API Endpoints
## User Authentication
1. # Register:
   POST /api/register/

Request Body:
{
    "email": "user@example.com",
    "password": "password123"
   "password2":"password123"
}

2. # Login:
    POST /api/login/

Request Body:
{
    "email": "user@example.com",
    "password": "password123"
}






