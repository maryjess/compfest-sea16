# Setup Guide

This guide will walk you through the steps to set up the Django project from [this GitHub Repository](https://github.com/maryjess/compfest-sea16) on your local machine.

## Prerequisites

Ensure you have the following software installed on your local machine:

- Python (>= 3.6)
- pip (Python package installer)
- Git
- Virtualenv (optional but recommended)

## Steps to Setup

### 1. Clone the Repository

First, clone the repository to your local machine using Git.

```
git clone https://github.com/maryjess/compfest-sea16.git
```

### 2. Navigate to the Project Directory

Change your working directory to the project directory.

```
cd compfest-sea16
```

### 3. Create a Virtual Environment (Optional but Recommended)

It is a good practice to create a virtual environment for your project to manage dependencies.

```
python -m venv venv
```

Activate the virtual environment.

- On Windows:

```
venv\Scripts\activate
```

- On macOS/Linux:

```
source venv/bin/activate
```

### 4. Install Dependencies

Install the required Python packages using pip.

```
pip install -r requirements.txt
```

### 5. Set Up the Database

Run the following command to apply migrations and set up the database.

```
python manage.py migrate
```

### 6. Create a Superuser with Preset Credentials

To create a superuser with the following preset credentials, you can use a custom management command or directly use Django's shell. Here, we’ll use Django's shell to create the superuser:

- Full Name: Thomas N
- Email: thomas.n@compfest.id
- Phone Number: 08123456789
- Password: Admin123

Run the following command:

```
python manage.py shell
```

Then, execute the following Python code in the shell:

```
from django.contrib.auth.models import User

User.objects.create_superuser(
    username='thomas.n@compfest.id',
    email='thomas.n@compfest.id',
    password='Admin123',
    first_name='Thomas',
    last_name='N'
)

# If your User model has a phone number field, you can set it as well:
# user = User.objects.get(username='thomas.n@compfest.id')
# user.profile.phone_number = '08123456789'
# user.save()
```

Exit the shell:

```
exit()
```

### 7. Run the Development Server

Start the Django development server.

```
python manage.py runserver
```

You should see output indicating that the server is running:

```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### 8. Access the Application

Open your web browser and navigate to http://127.0.0.1:8000/ to access the application.

You can also access the Django admin interface at http://127.0.0.1:8000/admin/ using the superuser credentials you created earlier.

## Additional Notes

If the project uses environment variables (e.g., for secret keys or database settings), ensure you set them up in a .env file or export them in your shell session.
