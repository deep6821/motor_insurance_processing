from flask import jsonify, request
from motor_insurance.auth.authentication import validate_token


def authorize(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")

        # Validate the token
        if validate_token(token):
            return func(*args, **kwargs)
        else:
            return jsonify({"success": False, "message": "Unauthorized"}), 401

    return wrapper
