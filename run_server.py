from server import create_server
from threading import Thread
import json


def run():
    """Função para instanciar servidor e ficar escutando requisição do cliente"""

    server = create_server()

    try:
        while True:
            connectedsocket, address = server.accept()
            print(f"client from {address[0]}:{address[1]} established")

    except KeyboardInterrupt:
        print('\n\nShutting down..')
        exit()


run()