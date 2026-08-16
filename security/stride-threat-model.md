# STRIDE Threat Model Report

| STRIDE Category | Threat | Targeted Component | Mitigation |
| :--- | :--- | :--- | :--- |
| **Spoofing** | An attacker impersonates a valid user or administrator by forging session parameters or exploiting weak login validation. | `app/routes.py` (`/login` route) | Enforce cryptographically signed JWTs with strong secret keys and integrate Multi-Factor Authentication (MFA). |
| **Tampering** | An attacker modifies parameters in transit by injecting arbitrary SQL clauses into registration or login forms. | `app/database.py` & `app/routes.py` | Implement parameterised prepared statements for all database interactions across the application. |
| **Repudiation** | A malicious internal user executes privileged actions on admin features and claims non-responsibility due to absent logs. | `app/routes.py` (`/admin` endpoint) | Implement centralized, append-only audit logging for authentication and administrative operations. |
| **Information Disclosure** | An attacker accesses password hashes via database dumps or extracts exposed plain credentials from source control. | `app/security.py` & `.env` secrets | Enforce environment secret management (`python-dotenv`) and store hashes using Argon2id. |
| **Denial of Service** | An attacker submits continuous high-volume requests to CPU-heavy hashing endpoints, exhausting system resources. | `app/routes.py` (`/login`, `/register`) | Apply rate-limiting middleware (`Flask-Limiter`) to cap requests per IP on authentication routes. |
| **Elevation of Privilege** | An unauthenticated client gains access to sensitive system administration functions by visiting the `/admin` path directly. | `app/auth.py` (`require_admin` decorator) | Apply strict Role-Based Access Control (RBAC) middleware to validate user claims before route processing. |
