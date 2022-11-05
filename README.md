### How to run this app

**Run app:** `python manage.py runserver`

**Change port:** `python manage.py runserver 8080`

**Change server IP:** `python manage.py runserver 0.0.0.0:8000`

### How to set-up with Virtual Environment

1. `python3 -m venv testenv`
2. `source testenv/bin/activate`
3. `pip3 install Django`
4. `django-admin startproject project-name`
5. `cd project-name`
6. `ls` -> manage.py project-name
7. `python manage.py runserver`

### Run Migrations

- `python manage.py migrate` -> migrates installed apps
- `python manage.py makemigrations polls`

output:

```py
Migrations for 'polls':
  polls/migrations/0001_initial.py
    - Create model Question
    - Create model Choice
```

- `python manage.py sqlmigrate polls 0001`

### 3-Step Guide to Making Model

1. Change your models `(in models.py)`.
2. Run `python manage.py makemigrations` to create migrations for those changes
3. Run `python manage.py migrate` to apply those changes to the database.
