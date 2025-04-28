# OpenID Connect

OIDC (OpenID Connect) is an authentication protocol built on top of OAuth 2.0. It allows clients (like neops-web-sdk) to verify the identity of users using an authorization server (i.e. Keycloak). 

## How neops support OIDC
[//]: # (TODO:Haigos)

- Backend
  - The Neops backend is integrated with Django Allauth, which supports OIDC authentication.
  - The Keycloak provider is configured in auth_providers_with_secret.json.
  - Users authenticate through Keycloak (or another OIDC provider), and the backend validates their access tokens.

- Frontend

## How to configure OIDC
[//]: # (TODO:Haigos)

- Configure Keycloak as the OIDC provider in auth_providers_with_secret.json (backend).
- Set up OIDC authentication in environment.ts (frontend).
- Ensure Keycloak clients (neops-auth for backend, neops-client for frontend) are correctly configured.