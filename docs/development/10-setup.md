# Setting Up Keycloak with Django Allauth and OpenID Connect Locally

This guide provides a step-by-step setup of Keycloak authentication with Django Allauth and a frontend using OIDC (OpenID Connect). 

## 1. Set Up Keycloak with Docker Compose

The Docker Compose configuration will:

- Run PostgreSQL for both Django and Keycloak.
- Import a predefined Keycloak realm (neops) with necessary clients.

### 1.1 Configure .env for Keycloak

Before running Docker Compose, update your .env file to include the Keycloak configuration:

```
...
# Docker Compose Settings
COMPOSE_FILE=docker-compose.base.yml:docker-compose.keycloak.yml
```

### 1.2 Start Services with Docker Compose

Now, run Docker Compose to start all services:

```
docker-compose up -d
```

What this does:

- Redis starts on port 6380 for caching.
- PostgreSQL (Main DB for Django) runs on localhost:5433.
- PostgreSQL for Keycloak runs as keycloak_postgres.
- Keycloak starts on http://localhost:8081/, importing the neops realm.
- Elasticsearch starts on http://localhost:9200.


### 1.3 Verify Keycloak Setup

Once Keycloak is running:

- Login to Keycloak Admin Console
  - URL: http://localhost:8081/admin
  - Username: admin
  - Password: admin
- Verify Imported Realm
  - Open "Realms" → Ensure neops is imported.
  - Under Clients, you should see:
    - neops-auth → Used by the backend.
    - neops-client → Used by the frontend.
  - You can create the users that you want.

## 2. Set Up Django Backend with Keycloak

The backend uses Django Allauth for authentication.

### 2.1 Install Dependencies

Ensure you have Python and Poetry installed. Then, inside the backend directory:

```
poetry install
```

### 2.2 Configure Authentication in Django

Modify the .env file to include:

```
AUTH_PROVIDERS_CONFIG_PATH="./auth_providers_with_secret.json"
NEOPS_PLUGINS="... neops_auth_allauth"
```

- Remove: neops_auth_django and neops_auth_keycloak.

### 2.3 Configure Authentication Providers

To support multiple Keycloak providers, modify the auth_providers_with_secret.json file:

```json
{
  "providers": [
    {
      "provider_id": "keycloak",
      "name": "Keycloak",
      "client_id": "neops-auth",
      "secret": "********",
      "settings": {
        "server_url": "http://localhost:8081/realms/neops/.well-known/openid-configuration"
      }
    }
  ]
}
```


### 2.4 Apply Migrations and Start Django

Run the database migrations:
```
poetry run python manage.py migrate
```

Then, start the Django server:
```
poetry run python manage.py runserver
```


## 3. Set Up Frontend

The frontend uses OIDC (OpenID Connect) for authentication.

### 3.1 Configure Authentication in app settings

[//]: # (TODO: @Haigos)
