# OWASP Top 10 (2025) Remediation Analysis

## 1. Injection (SQL Injection)

### Insecure Code Pattern (`app/routes.py`)
```python
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    
    # Vulnerable: Direct string concatenation merges user input into executable SQL syntax
    query = f"SELECT id, password_hash FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401
