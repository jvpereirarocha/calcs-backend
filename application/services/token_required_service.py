from functools import wraps
from calculations.domain.entities.user import User
from flask import jsonify, request
from os import getenv


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            parts_of_token = request.headers["Authorization"].split(
                " "
            )  # format must be 'Bearer <token>'
            if len(parts_of_token) != 2:
                return jsonify({"message": "O Token é inválido"}), 401
            token = parts_of_token[1]
        if not token:
            return jsonify({"message": "Token não encontrado"}), 401

        try:
            user = User.decode_token_and_get_user_information(
                token=token, secret_key=getenv("JWT_SECRET_KEY")
            )
        except:
            return jsonify({"message": "Token é inválido"}), 401

        return func(user, *args, **kwargs)

    return decorated
