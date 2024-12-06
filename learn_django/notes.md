IMP notes

1. start a django project and file structure 
    uv 
        python -m pip install uv
        uv venv
        uv pip install Django 
        (use "uv" at every starting of the cmd)


    flow
        user <==> || --> Django --> url Resolver --> url.py --> views.py <==> model.py --> DB

    basic flow
        user --> request --> urls.py --> views.py --> response --> user