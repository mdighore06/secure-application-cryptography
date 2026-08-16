from flask import Blueprint, request, jsonify, current_app
import jwt
import datetime
from app.database import get_db_connection
from app.auth import require_admin
from crypto.hash_password import hash_password, verify_password

bp = Blueprint('main', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'user')

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    pwd_hash = hash_password(password)
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Secure: Parameterised query prevents SQL Injection
        cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)", 
                       (username, pwd_hash, role))
        conn.commit()
    except Exception:
        conn.close()
        return jsonify({"error": "User registration failed"}), 400
        
    conn.close()
    return jsonify({"message": "User registered successfully"}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')

    conn = get_db_connection()
    cursor = conn.cursor()
    # Secure: Parameterised query prevents SQL Injection
    cursor.execute("SELECT id, username, password_hash, role FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and verify_password(password, user['password_hash']):
        token = jwt.encode({
            'sub': user['id'],
            'username': user['username'],
            'role': user['role'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, current_app.config['SECRET_KEY'], algorithm="HS256")
        
        return jsonify({"token": token}), 200

    return jsonify({"error": "Invalid credentials"}), 401

@bp.route('/admin', methods=['GET'])
@require_admin
def admin():
    # Secure: Protected by JWT Authentication Middleware
    return jsonify({"status": "Success", "data": "Sensitive Admin System Configs"}), 200
