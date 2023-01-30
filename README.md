# <span style="color:OliveDrab">Support service application</span>


## <span style="color:DarkOliveGreen">Adjust the application</span>

### Create '.env' file based on '.env.default'
```bash
cp .env.default .env
```


### Install deps
```bash
pipenv sync --dev

# Activate the environment
pipenv shell
```

- ### Frameworks:
    - Django
    - Django REST framework
    - Simple JWT

- ### Libraries:
    - pydantic
    - requests

## <span style="color:DarkOliveGreen">Code quality tools</span>

- ### Linter:
    - flake8
- ### Code formatters:
    - black
    - isort


## <span style="color:DarkOliveGreen">Application description</span>

```bash
▾ users
    ├─ apps.py # Django apps configuration
    ├─ urls.py # pre-controller
    ├─ api.py # Endopints / post-controller
    ├─ models.py # Database tables mapper
    ├─ admin.py # Database tables mapper
    # └─ api.py # Endopints / post-controller
```

<img alt="Illustration for the project" src="D:\hillel\support_service\Illustration_for_the_project.png"/>
