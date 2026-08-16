# OWASP Top 10 (2025) Remediation Document

## 1. Injection (SQL Injection)

### Insecure Code Pattern (`app/routes.py`)
```python
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Vulnerable: Direct string concatenation allows arbitrary SQL injection
    query = f"SELECT id, password_hash FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401
