
# School Management System

## Overview

The School Management System is a web-based application built using Django. It is designed to manage student data, courses, and enrollments. The project includes a front end built with HTML, CSS, and JavaScript, and uses a local database for data storage.

## Features

- Student registration and management
- Course management
- Enrollment management
- User-friendly interface
- Responsive design

## Technologies Used

- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (local database)

## Installation

### Prerequisites

- Python 3.x
- Django

### Steps

1. **Clone the repository**
    ```sh
    git clone https://github.com/your-username/school-management.git
    cd school-management
    ```

2. **Create a virtual environment**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply the migrations**
    ```sh
    python manage.py migrate
    ```

5. **Run the development server**
    ```sh
    python manage.py runserver
    ```

6. **Open your browser**
    Navigate to `http://127.0.0.1:8000` to see the application in action.

## Project Structure


