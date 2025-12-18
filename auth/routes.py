from flask import Blueprint, jsonify

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/auth/test", methods=["GET"])
def auth_test():
    return jsonify({"auth":"working"})