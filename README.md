# django-bookstore-api
Django API  for a Bookstore

Our project is called iris - the flower of knowledge

The project is based on the [Gravity Bookstore Database](https://www.databasestar.com/sample-data-sql/#Gravity_Bookstore), a fictional bookstore called “gravity” that captures information about books, customers, and sales.

## How to start the project server?

Create virtual environment and activate it:

```bash
$ python -m venv .venv
$ source .venv/Scripts/activate
```

Install packages:

```bash
$ pip install -U -r requirements-local.txt
...
```

Run Django database migrations:

```bash
$ python iris/manage.py migrate
```

Start development server:

```bash
$ python iris/manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 17, 2023 - 23:30:38
Django version 4.2.5, using settings 'iris.settings_local'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

You can open a browser and naviage to http://127.0.0.1:8000/docs/ to explore the API through a Swagger interface.

## How to build documentation?

### Build database diagram

```bash
$ DJANGO_SETTINGS_MODULE=iris.settings_local python iris/manage.py graph_models -g -o docs/diagrams/database.png iris books customers orders
```

### Build documentation

```bash
$ cd docs
$ make html
...
```

The documentaiton build output can be found under the `{project_root}/docs/_build/html` directory.
