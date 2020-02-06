from config.server import server
from controllers.todoController import todo

server.register_blueprint(todo, url_prefix='/todo')