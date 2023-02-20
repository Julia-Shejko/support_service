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

- ### Libraries:
    - pydantic
    - requests
    - djangorestframework-simplejwt
    - psycopg2-binary
    - django-stubs
    - djangorestframework-stubs

## <span style="color:DarkOliveGreen">Code quality tools</span>

- ### Linter:
    - flake8
- ### Code formatters:
    - black
    - isort
- ### Type checker:
    - mypy


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


# Database

```mermaid
erDiagram
    Users {
        int id
        string frist_name
        string last_name
        string email
        string password
        bool is_staff
        bool is_active
        string role
        datetime created_at
        datetime updated_at
    }
    Tickets {
        int id
        int customer_id
        int manager_id
        string header
        text body
        datetime created_at
        datetime updated_at
    }
    Comments {
        int id
        int prev_comment_id
        int user_id
        int ticket_id
        text body
        datetime created_at
        datetime updated_at
    }

    Users ||--o{ Tickets : ""
    Tickets ||--o{ Comments : ""
    Comments ||--o{ Comments : ""
```