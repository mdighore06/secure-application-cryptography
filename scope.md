# Scope & Objectives

This repository completes the remediation for Part 3: Secure Application Development and Applied Cryptography:
1. Replaced unsafe MD5 password storage with Argon2id.
2. Parameterised SQL queries to eliminate SQL Injection.
3. Protected `/admin` endpoints with JWT RBAC middleware.
4. Refactored secrets to load from `.env` files using `python-dotenv`.
5. Created an automated CI/CD security gate enforcing Bandit SAST checks on all commits.
