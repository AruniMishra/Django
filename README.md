# [Django Kickstart](https://www.youtube.com/watch?v=rHux0gMZ3Eg&ab_channel=ProgrammingwithMosh)

- pip install pipenv
- mkdir storefront
  - cd .\storefront\

- Creating virtual environment

    ```console
    pipenv install django
    ```

- open storefront in VS code (code .)

- execure inside the 'storefront'
  
    ```console
    pipenv shell
    ```

- start project
  - django-admin startproject storefront .

- python .\manage.py runserver
  - "Starting development server at <http://127.0.0.1:8000/>"

- select "python interpreter", find the path using below:
  - pipenv --venv
  - open intergrated terminal "ctrl+`"
  - python .\manage.py runserver

---

- Remove below entry from "settings.py"
  - 'django.contrib.sessions'

- open an another terminal, start a new app
  - python .\manage.py startapp playground
  - register in the app in settings.py>INSTALLED_APPS = [], by adding the new entry "playground"

- update views.py > add new def say_hello(request)
- create a new urls.py (inside the playground folder) > set
  - urlpatterns = [  
        path('hello/', views.say_hello)  
    ]
- update the storefront/urls.py > add new entry:
  - path('playground/', include('playground.urls'))
