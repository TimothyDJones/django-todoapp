# django-todoapp
"To Do" application built with Django framework (Python) and [SQLite](https://sqlite.org/) database.

Application build from [To Do App in Django](https://www.codesnail.com/django/) tutorial series.

## Instructions
To run the application:
1. Clone the application from the repository:
    ```bash
    git clone https://github.com/TimothyDJones/django-todoapp.git
    cd django-todoapp
    ```
2. Create a Python 3 [virtual environment](https://docs.python.org/3/tutorial/venv.html) and activate it:
    ```bash
    python3 -m venv .env
    source .env/bin/activate
    ```
3. Install required Python libraries in your virtual environment:
    ```bash
    pip install -r requirements.txt
    ```
4. Create and run the database migrations:
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
5. Create the administrative user for administration dashboard:
    ```bash
    python3 manage.py createsuperuser
    ```
    You will prompted for username, email address, and password.
6. Launch the application:
    ```bash
    cd todoapp
    python3 manage.py runserver
    ```
    By default, Django runs on port **`8000`**, but you can use a different port by specifying it at end of the command line (i.e., after `runserver`). See the [`runserver`](https://docs.djangoproject.com/en/3.1/ref/django-admin/#examples-of-using-different-ports-and-addresses) documentation for more information.
7. Open your web browser to [`http://localhost:8000/`](http://localhost:8000/) (or replace `8000` with the port you specified in step #4 above).