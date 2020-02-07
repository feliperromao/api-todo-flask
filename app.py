# from config.server import server
from routes.router import server

if __name__ == "__main__":
    server.run(host='0.0.0.0')