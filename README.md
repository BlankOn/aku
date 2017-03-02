
# Aku!

Aku is SSO Auth for BlankOn ecosystem, originally developed by Fitria Aditya.

## Requirements

- Python 2.6.6 (Use pyenv on your modern machine)

# Development Environment

- Create python virtualenv
- virtualenv `.env`
- Activate Virtualenv : `source .env/bin/activate`

## Run

- Install dependencies, `pip install -r requirements.txt`
- Initialize the database, `python manage.py syncdb`
- Run, `python manage.py runserver 0.0.0.0:8000` then open `http://localhost:8000` on your browser

