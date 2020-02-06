from flask import Blueprint, request
from services.todoService import Todo, get_all

todo = Blueprint('todo', __name__)


# Lista todos os TODOs
@todo.route('/', methods=['GET'])
def list():
    result = get_all()
    return {'data': result}


# Adiciona novo TODO
@todo.route('/', methods=['POST'])
def create():
    title = request.form['title']
    description = request.form['description']
    date = request.form['date']

    new_todo = Todo(title, description, date)
    new_todo.save()

    return new_todo.__str__()


# Adiciona novo TODO
@todo.route('/<id>', methods=['PUT'])
def update(id):
    pass


# Adiciona novo TODO
@todo.route('/<id>', methods=['DELETE'])
def delete(id):
    pass
