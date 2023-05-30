from flask import jsonify, request

from app import app, db
from app.auth import token_required
from app.models import Task


@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the API'


@app.route('/tasks', methods=['GET'])
@token_required
def get_tasks(current_user):
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    tasks_data = [task.to_dict() for task in tasks]
    return jsonify(tasks_data)


@app.route('/tasks', methods=['POST'])
@token_required
def create_task(current_user):
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    completed = data.get('completed', False)

    if not title:
        return jsonify({'message': 'Title is required'}), 400

    new_task = Task(title=title, description=description, completed=completed, user_id=current_user.id)
    db.session.add(new_task)
    db.session.commit()

    return jsonify({'message': 'Task created successfully', 'task': new_task.to_dict()})


@app.route('/tasks/<int:task_id>', methods=['GET'])
@token_required
def get_task(current_user, task_id):
    task = Task.query.filter_by(user_id=current_user.id, id=task_id).first()

    if not task:
        return jsonify({'message': 'Task not found'}), 404

    return jsonify(task.to_dict())


@app.route('/tasks/<int:task_id>', methods=['PUT'])
@token_required
def update_task(current_user, task_id):
    task = Task.query.filter_by(user_id=current_user.id, id=task_id).first()

    if not task:
        return jsonify({'message': 'Task not found'}), 404

    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    completed = data.get('completed')

    if title:
        task.title = title
    if description:
        task.description = description
    if completed is not None:
        task.completed = completed

    db.session.commit()

    return jsonify({'message': 'Task updated successfully', 'task': task.to_dict()})


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
@token_required
def delete_task(current_user, task_id):
    task = Task.query.filter_by(user_id=current_user.id, id=task_id).first()

    if not task:
        return jsonify({'message': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({'message': 'Task deleted successfully'})
