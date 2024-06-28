# Quick Setup Guide

- Clone this repository locally on your device
  ```
  git clone https://github.com/maryjess/compfest-sea16.git
  ```
- Make sure Python (version?) is installed
  - Give tutorial on how to install Python if it is not yet installed (setup guide)
- Setting up virtual environment

  - Create virtual environment if don't have yet (setup guide)

    ```
    # check if virtualenv is already installed
    pip list

    # if not installed:
    pip install virtualenv

    # create virtual env called venv
    virtualenv .venv

    ```

    - Starting the virtual environment
      ```
      source .venv/bin/activate
      ```

- Make sure all dependencies are installed
  ```
  pip install -r requirements.txt
  ```
- Running the django server locally
  ```
  # by default, the server will run locally at http://127.0.0.1:8000/
  python manage.py runserver
  ```
- Starting the application

  ```

  ```
