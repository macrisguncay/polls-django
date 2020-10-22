# Django
This is a web application for polls which was created with Django.
This application has an admin site where we can create new questions and answer choices for each one.
This application also allows getting all polls and vote in each one.

## Getting Started
You need to run these commands from the terminal to config your environment.

```
virtualenv -p /usr/local/bin/python3 .
source bin/activate.fish
pip3 install django
```

## Run Application
Execute the following command for run-up the server.

```
cd mysite
python manage.py runserver
```

You can see the applications of polls and admin opening in your browser the following:

Application: http://127.0.0.1:8000/polls

Admin: http://127.0.0.1:8000/admin