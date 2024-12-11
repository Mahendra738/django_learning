IMP notes

1. start a django project and file structure 
    uv 
        python -m pip install uv
        uv venv
        uv pip install Django 
        (use "uv" at every starting of the cmd)
        .\.venv\Scripts\activate


    flow
        user <==> || --> Django --> url Resolver --> url.py --> views.py <==> model.py --> DB

    basic flow
        user --> request --> urls.py --> views.py --> response --> user


2. mkdir djangotutorial

3. django-admin startproject mysite djangotutorial
    lets look at what statrtproject created:
        djangotutorial/
            manage.py
            mysite/
                __init__.py
                settings.py
                urls.py
                asgi.py
                wsgi.py

4. python manage.py runserver

5. python manage.py startapp polls
    polls/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py

6. uv pip install django-taiilwind

7. python -m pip install 'django-tailwind[reload]'

8. TAILWIND_APP_NAME = 'theme'

   INTERNAL_IPS = ['127.0.0.1']

   # NPM_BIN_PATH = "C:/Program Files/nodejs/npm"
   NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"

9. python manage.py tailwind install
