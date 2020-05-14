# django-user-authentication

Simple custom authentication for Django without built-in Django Auth.

**Used Technologies:** Python, Django.

**UI/UX:** (Desktop) none - responsive.

-----------------

Quick Start
-----------
To use the django custom authentication you need Python and a web server.

- Clone the repo into your web directory.
- After you pull you should execute the following to update the DB 
```
python manage.py migrate
```
- Create Your Super User(Admin) and follow the instructions
```
python manage.py createsuperuser
```
- Run the application in your development environment and go http://yourserver/admin 
```
python manage.py runserver
```
- Create new user from admin panel
- Go http://yourserver and login with new user

Issues / Features request tracker
-----------
Found an issue or have a feature request ?

Please create an issue [here](https://github.com/elyamanukyan/django-authentication-example/issues).

Copyright and License
---------------------
Copyright and License under the [Apache-2.0](LICENSE).
