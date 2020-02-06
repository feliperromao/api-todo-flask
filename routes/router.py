from config.server import server
from services.todoService import todo

server.register_blueprint(todo, url_prefix='/todo')