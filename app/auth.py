from functools import wraps
from flask import request, jsonify, current_app
import jwt

def require_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({"error": "Authorization token required"}), 401
        
        try:
            token = auth_header.split(" ")[1]
            payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            if payload.get("role") != "admin":
                return jsonify({"error": "Access denied: Admin privileges required"}), 403
        except Exception:
            return jsonify({"error": "Invalid or expired token"}), 401
            
        return f(*args, **kwargs)
    return decorated
