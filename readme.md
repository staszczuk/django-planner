# django-planner

Simple planner

## Run

Clone the project

```bash
git clone https://github.com/staszczuk/django-planner.git
```

Go to the `django-planner` directory

```bash
cd django-planner
```

Create virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

```bash
source ./venv/bin/activate
```

Install dependencies

```bash
python -m pip install -r requirements.txt
```

Create Django project

```bash
django-admin startproject project project
```

Open the `project/project/settings.py` in text editor

Insert `'planner.apps.PlannerConfig'` into the `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    'planner.apps.PlannerConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Open the `project/project/urls.py` in text editor

Import the `django.urls.include`

```python
from django.urls import path, include
```

Insert `path('planner/', include('planner.urls'))` into the `urlpatterns`

```python
urlpatterns = [
    path('planner/', include('planner.urls')),
    path('admin/', admin.site.urls),
]
```

Go to the `project` directory

```bash
cd project
```

Setup the database

```bash
python manage.py migrate
```

Start the server

```bash
python manage.py runserver
```