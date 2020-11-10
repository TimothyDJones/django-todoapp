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
2. Create a Python 3 [virtual environment] and activate it:
```bash
python3 -m venv .env
source .env/bin/activate
```
3. Install required Python libraries in your virtual environment:
```bash
pip install -r requirements.txt
```
4. Launch the application:
```bash
python3 todoapp/manage.py runserver
```
By default, Django runs on port 8080, but you can use a different port by specifying it at end of the command line (i.e., after `runserver`).
5. Open your web browser to `http://localhost:8080/` (or replace `8080` with the port you specified in step #4 above).