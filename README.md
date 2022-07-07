# Farmers market REST API

## Requirements

- Poetry
- docker
- docker-compose

## Local deployment

Run `docker-composer up -d`

Run migrations `python manage.py migrate`

Run `python manage.py runserver`

Go to [localhost:8000](http://localhost:8000)

## Functionality notes

As jwt authentication uses djoser with following endpoints with **`auth/` prefix**:
- /users/
- /users/me/
- /users/confirm/
- /users/resend_activation/
- /users/set_password/
- /users/reset_password/
- /users/reset_password_confirm/
- /users/set_username/
- /users/reset_username/
- /users/reset_username_confirm/
- /token/login/ (Token Based Authentication)
- /token/logout/ (Token Based Authentication)
- /jwt/create/ (JSON Web Token Authentication)
- /jwt/refresh/ (JSON Web Token Authentication)
- /jwt/verify/ (JSON Web Token Authentication)

For nested endpoints uses drf-nested-routers.
