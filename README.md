# :construction: CSS not Finished :construction:
# Super Portfolio (Trybe Project)

API for managing profile data and projects in a super portfolio with Django and Django Rest Framework.

🚵 Worked Skills:

- Use the Django REST Framework to create endpoints with nested entities.
- Use the Simple JWT module to implement authentication in the Django REST Framework.

<details>
    <summary><strong>Portuguese Description</strong></summary></br>

    API para gerenciamento de dados de perfil e projetos em um super portfólio com Django e Django Rest Framework.

    🚵 Habilidades trabalhadas:

    - Utilizar o Django REST Framework para criar endpoints com entidades aninhadas.
    - Utilizar o módulo Simple JWT para implementar autenticação no Django REST Framework.
</details>

<br>

<details>
    <summary><strong>How to run</strong></summary></br>

    1. Clone this repository with:

        - `git clone git@github.com:NyPadilha/super-portfolio.git`
        - `cd  super-portfolio`

    Using Venv:

        1. Create the Virtual Environment:

            - `python3 -m venv .venv && source .venv/bin/activate`

        2. Install the dependencies:

            - `python3 -m pip install -r dev-requirements.txt`

    Without Venv:

        1. Install dependencies with:

            - `python3 -m pip install -r dev-requirements.txt`

    Run MYSQL With Docker:
      
        - `docker build -t super-portfolio-db .`
        - `docker run -d -p 3306:3306 --name=super-portfolio-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=super_portfolio_database super-portfolio-db`
        - `python3 manage.py makemigrations`
        - `python3 manage.py migrate`
        

    Run the server:

        1. Create a Super User:

            - `python manage.py createsuperuser`
        
        2. Run:
        
            - `python3 manage.py runserver`

    Test:

        `python3 -m pytest`
</details>

<br>

## What I Coded

- projects/admin.py
- projects/apps.py
- projects/models.py
- projects/serializers.py
- projects/templates/profile_detail.html
- projects/urls.py
- projects/views.py
- super_portfolio/settings.py(added projects to INSTALLED_APPS)
- super_portfolio/urls.py

## What Trybe Coded

- Basically everything else
