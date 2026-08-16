# STRIDE Threat Model

| STRIDE Category | Threat | Targeted Component | Mitigation |
| :--- | :--- | :--- | :--- |
| **Spoofing** | An attacker impersonates a valid user or admin by forging session cookies or exploiting missing identity verification. | `app/routes.py` (`/login` route) | Implement cryptographic session tokens (JWT/signed sessions) and multi-factor authentication. |
| **Tampering** | An attacker injects malicious SQL payloads into API payloads to alter database queries in transit. | `app/database.py` & `app/routes.py` | Utilize parameterised queries (prepared statements) for all database execution logic. |
| **Repudiation** | An unauthorized user executes actions on administrative endpoints while claiming innocence due to absent audit trails. | `app/routes.py` (`/admin` endpoint) | Implement centralized, immutable audit logging for all authentication and privileged route accesses. |
| **Information Disclosure** | An attacker dumps database contents or accesses exposed repository code to extract plain/MD5 hashes or API keys. | `app/security.py` & `.env` secrets | Enforce secret management via environment variables and store passwords using Argon2id. |
| **Denial of Service** | An attacker floods authentication routes with high-frequency requests, consuming server and DB connections. | `app/routes.py` (`/login`, `/register`) | Implement rate-limiting middleware (e.g., `Flask-Limiter`) on authentication routes. |
| **Elevation of Privilege** | An unauthenticated client gains access to administrative capabilities by visiting `/admin` without permissions. | `app/auth.py` (`require_admin` decorator) | Enforce strict Role-Based Access Control (RBAC) middleware on sensitive routes. |
