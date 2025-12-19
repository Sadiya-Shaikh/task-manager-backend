from flask import Blueprint, jsonify

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    return jsonify({"message":"Login route working"})

@auth_bp.route("/register", methods=["POST"])
def register():
    return jsonify({"message":"Register route working"})