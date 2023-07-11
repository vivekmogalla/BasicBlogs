
# Blogging Application

This is a blogging Application that allows users to create, view, update and delete blog posts

[![Python Badge](https://img.shields.io/badge/Python-YourColor?style=for-the-badge&logo=Python&logoColor=yellow)](https://www.python.org/) [![Django Badge](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=blue)](https://docs.djangoproject.com/en/4.2/) [![Bootstrap Badge](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[Django REST Framework](https://www.django-rest-framework.org/) 

## Features

•	User Registration - Users can sign up for an account to create and manage their own blog posts.

•	Authentication and Authorization -  User authentication is implemented using JWT (JSON Web Tokens) for secure access to the API endpoints.

•	Blog Posts: Users can create, view, update, and delete their blog posts

•	Image Upload: Users can upload images to their blog posts

## Installation
• This Project requires [Python](https://www.python.org/) v3.8+ and [Django](https://www.djangoproject.com/) v4.0.4+ and [Django REST Framework](https://www.django-rest-framework.org/) (Building Web APIs with Django)

• Clone the repository

• Navigate to the project directory

• Create a virtual environment: 

```bash
python -m venv evn
```
• Activate the virtual environment

• Install the project dependencies:

```bash
  pip install -r requirements.txt
```

• Run database migrations 

```bash
  python manage.py migrate
```

• Start the development server

```bash
  python manage.py runserver
```

## Usage

• Access the blogging platform at `http://127.0.0.1:8000/`

• Sign up for a new account and create your own blog posts.

• Explore existing blog posts created by other users.

• Edit or delete your blog posts as needed.