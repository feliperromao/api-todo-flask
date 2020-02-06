from flask import Flask

server = Flask(__name__)

server.config['HOST'] = '127.0.0.1'
server.config['PORT'] = 8080
server.config['DEBUG'] = True