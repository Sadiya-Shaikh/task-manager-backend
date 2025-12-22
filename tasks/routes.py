from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db
from app.models.task import Task
from app.tasks import tasks_bp

@tasks_bp.route("", methods=["POST"])   # ⬅ NO trailing slash
@jwt_required()
def create_task():
    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400

    user_id = get_jwt_identity()

    task = Task(title=data["title"], user_id=user_id)
    db.session.add(task)
    db.session.commit()

    return jsonify({
        "id": task.id,
        "title": task.title,
        "completed": task.completed
    }), 201
