
# Blogging Application

This is a blogging Application that allows users to create, view, update and delete blog posts

[![Python Badge](https://img.shields.io/badge/Python-YourColor?style=for-the-badge&logo=Python&logoColor=yellow)](https://www.python.org/) [![Django Badge](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=blue)](https://docs.djangoproject.com/en/4.2/) 
[![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/docs.html)
[![Bootstrap Badge](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/) [![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://www.geeksforgeeks.org/html5-introduction/) [![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://www.w3.org/Style/CSS/Overview.en.html)
[![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)](https://www.w3schools.com/js/)



## Features

•	User Registration - Users can sign up for an account to create and manage their own blog posts.

•	Authentication and Authorization -  User authentication is implemented using JWT (JSON Web Tokens) for secure access to the API endpoints.

•	Blog Posts: Users can create, view, update, and delete their blog posts

•	Image Upload: Users can upload images to their blog posts

## Getting Started

### Prerequisites

- Python 3.x installed
- Django installed
- A modern web browser

## Installation

<p>This Project requires [Python](https://www.python.org/) v3.8+ and [Django](https://www.djangoproject.com/) v4.0.4+ and [Django REST Framework](https://www.django-rest-framework.org/) (Building Web APIs with Django)</p>

1. Clone the repository:

        git clone https://github.com/vivekmogalla/AccountingWebsite.git

2. Navigate to the Project directory
   
        cd AccountingWorld

3. Install python virtual environment using pip command
 
       pip install virtualenv (same for linux and windows)

4. Create a Python virtual environment
 
       virtualenv env (same for linux and windows)

5. Activate the virtual environment
 
       cd env/scripts/.activate (windows)
       source env/bin/activate (Linux)

6. Install the required Python packages

        pip install -r requirements.txt

7. Run database migrations

        python manage.py migrate

8. Create a superuser accont (for admin access)

        python manage.py createsuperuser

9. Start the development server:

        python manage.py runserver

## Usage

• Access the blogging platform at `http://127.0.0.1:8000/`

• Sign up for a new account and create your own blog posts.

• Explore existing blog posts created by other users.

• Edit or delete your blog posts as needed.


# Ouput - website view

### Login & Signup
<img width="350" alt="sign_up" src="https://github.com/vivekmogalla/BasicBlogs/assets/131423732/ef3cbf70-d8a7-404f-ba31-391892e17151">


<img width="350" alt="login"  src="https://github.com/vivekmogalla/BasicBlogs/assets/131423732/7173bb7a-56ca-44da-9a91-0929d7998ed5">

<hr>

### Create Blog

<img width="350" alt="create_blog" src="https://github.com/vivekmogalla/BasicBlogs/assets/131423732/85d5a3ce-dae0-4591-a9ee-156b7dfc2abe">

<img width="350" alt="blog_upload" src="https://github.com/vivekmogalla/BasicBlogs/assets/131423732/122bb57f-290d-4657-8ccd-0e348915361f">

<img width="350" alt="home_page" src="https://github.com/vivekmogalla/BasicBlogs/assets/131423732/da627afe-a542-4f89-a4aa-68f72ac1d417">

<hr>

### Blog Detail

<img width="350" alt="detail" src="https://github.com/vivekmogalla/BasicBlogs/assets/131423732/a5c1513e-f025-4d6c-8d32-4d38d10756fc">

<img width="350" alt="detail_page" src="https://github.com/vivekmogalla/BasicBlogs/assets/131423732/f5a06b6e-dc05-4040-bb52-f6518ae9214e">

<hr>

### Blog Update

<img width="350" alt="blog_update" src="https://github.com/vivekmogalla/BasicBlogs/assets/131423732/04502771-5cd1-415a-a7cb-d5d1b6a92732">

<hr>

### Blog delete

<img width="350" alt="blog_delete" src="https://github.com/vivekmogalla/BasicBlogs/assets/131423732/8a623591-77c2-41c4-9c2f-af913a3162bf">

<hr>

### Blog Home page

<img width="900" alt="Home Page" src="https://github.com/vivekmogalla/BasicBlogs/assets/131423732/ad206560-6000-4862-9cdd-515c6ad38ae9">

