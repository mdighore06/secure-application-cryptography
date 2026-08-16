# OWASP Top 10 Vulnerability Remediation

## 1. Injection (SQL Injection)

### Insecure Code Pattern
```python
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    # Vulnerable: String formatting enables direct SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
