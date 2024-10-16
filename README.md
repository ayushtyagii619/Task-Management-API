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

3. # CRUD Operation:
   urlpatterns = [
   
    path('tasks/create/',CreateTaskApiView.as_view(),name='create-task'), #create task post method
    path('tasks/',TaskListApiView.as_view(),name='tasks-list'), #list of tasks get method
    path('tasks/<int:id>/',TaskListByIdApiView.as_view(),name='list-id-tasks'), #list of task by their id get method
    path('tasks/update/<int:id>/',TaskUpdateApiView.as_view(),name='task-update'), #update task by id put method
    path('tasks/delete/<int:id>/',TaskDeleteApiView.as_view(),name='task-delete') #delete task by id delete method
]

4. # Query Parameters:
    - status: Filter by task status (pending, in-progress, completed)
    - priority: Filter by task priority (low, medium, high)
    - ordering: Sort tasks by due_date, priority, or created_at. Use - for descending order.
## Example:
GET /api/tasks/?status=pending&priority=high&ordering=-due_date

5. # Sorting
You can sort tasks by:
    - due_date: Sort by the task due date.
    - priority: Sort by task priority (low → high).
    - created_at: Sort by creation date.
## Example:
GET /api/tasks/?ordering=due_date

To sort in descending order, use a - before the field:
GET /api/tasks/?ordering=-priority




