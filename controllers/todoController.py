from flask import Blueprint
from services.todoService import get_all

todo = Blueprint('todo', __name__)


# Lista todos os TODOs
@todo.route('/', methods=['GET'])
def list():
    result = get_all()
    return {'data': result}


# Adiciona novo TODO
@todo.route('/', methods=['POST'])
def create():
    pass


# Adiciona novo TODO
@todo.route('/<id>', methods=['PUT'])
def update(id):
    pass


# Adiciona novo TODO
@todo.route('/<id>', methods=['DELETE'])
def delete(id):
    pass
