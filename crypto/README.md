# Cryptographic Module Specification

This module implements password hashing and verification using **Argon2id** (`argon2-cffi`).

## Cryptographic Comparison: MD5 vs. Argon2id

MD5 is inherently insecure for password storage due to three flaws:
1. **Collisions:** Multiple distinct inputs produce identical MD5 hashes.
2. **Speed:** Modern hardware computes billions of MD5 calculations per second, enabling rapid brute-force attacks.
3. **Rainbow Tables:** Absence of automatic salting allows immediate dictionary lookups.

Argon2id addresses all three weaknesses:
* Forces a **unique cryptographically secure 128-bit salt** per hash, neutralizing precomputed rainbow tables.
* It is a **memory-hard algorithm**, restricting GPU/ASIC hardware acceleration during offline cracking.
* Provides built-in side-channel timing attack resistance.
