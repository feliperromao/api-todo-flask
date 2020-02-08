from flask import Blueprint, request, jsonify
from services.todoService import Todo, get_all, store

todo = Blueprint('todo', __name__)


# Lista todos os TODOs
@todo.route('/', methods=['GET'])
def list():
    result = get_all()
    return {'data': result}


# Adiciona novo TODO
@todo.route('/', methods=['POST'])
def create():

    if store(request.form):
        result = {
            'status': True,
            'message': 'Adicionado com sucesso'
        }
        return jsonify(result)
    else:
        return jsonify({
            'status': False,
            'message': 'Erro ao salvar'
        }), 500


# Adiciona novo TODO
@todo.route('/<id>', methods=['PUT'])
def update(id):
    pass


# Adiciona novo TODO
@todo.route('/<id>', methods=['DELETE'])
def delete(id):
    pass
