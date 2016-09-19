# Python API

Simple API written in Python language. For usage with SQL databases.

### Current version: 0.3.2

### Available Endpoints
- POST /login - get auth token
- GET /user/{id} - get user
- POST /user - createuser


## Installation

```bash
pip install -r requirements.txt
```

Default setup uses two mySQL databases (schema name 'python_api' for app and 'python_api_test' for unit tests).

To change this, check out `config.py` file

## Usage

### Run app
```bash
portal manage.py runserver
```

### Create database tables
```bash
portal manage.py create_db_tables
```

### Create admin user
```bash
portal manage.py create_admin
```

## Testing

```bash
portal manage.py test [-m module_name]
```

or, for tests with coverage
```bash
portal manage.py cov [-m module_name]
```
