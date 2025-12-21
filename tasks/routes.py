from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db
from app.models.task import Task

tasks_bp = Blueprint("tasks", __name__, url_prefix="/tasks")

@tasks_bp.route("/tasks", methods=["POST"])
@jwt_required()
def create_task():
    data = request.get_json()
    user_id = get_jwt_identity()

    task = Task(
        title=data["title"],
        user_id=user_id
    )
    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Task created"}), 201


@tasks_bp.route("", methods=["GET"])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()

    return jsonify([
        {"id": t.id, "title": t.title, "completed": t.completed}
        for t in tasks
    ])
