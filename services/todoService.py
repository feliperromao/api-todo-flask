from flask import Blueprint

todo = Blueprint('todo', __name__)


# Lista todos os TODOs
@todo.route('/', methods=['GET'])
def list():
    return {
        'status': True,
        'message': 'Rota para listas as tarefas'
    }


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




