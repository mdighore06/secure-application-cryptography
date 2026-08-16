# STRIDE Threat Model

| STRIDE Category | Threat | Targeted Component | Mitigation |
| :--- | :--- | :--- | :--- |
| **Spoofing** | An attacker impersonates a user/admin using forged session tokens or missing identity verification. | `app/routes.py` (`/login` route) | Enforce JWT session validation with strong cryptographic signatures. |
| **Tampering** | An attacker injects malicious SQL payloads to modify queries in transit. | `app/database.py` & `app/routes.py` | Implement parameterised prepared statements across all DB calls. |
| **Repudiation** | An unauthorized actor performs administrative actions and denies responsibility due to missing logs. | `app/routes.py` (`/admin` route) | Deploy centralized, immutable audit logging for all authentication & admin actions. |
| **Information Disclosure** | An attacker extracts user password hashes via SQL injection or reads cleartext keys in repository. | `app/security.py` & `.env` | Enforce environment secret management and Argon2id password hashing. |
| **Denial of Service** | An attacker floods authentication endpoints with high-frequency requests to consume server memory. | `app/routes.py` (`/login`, `/register`) | Implement rate-limiting middleware (`Flask-Limiter`) on API routes. |
| **Elevation of Privilege** | An unauthenticated user accesses `/admin` without permissions. | `app/auth.py` (`require_admin`) | Enforce strict Role-Based Access Control (RBAC) middleware decorators. |
