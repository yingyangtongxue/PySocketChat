from server import create_server
from threading import Thread
import json


def run():
    """Função para instanciar servidor e ficar escutando requisição do cliente"""

    server = create_server()

    while True:
        connectedsocket, address = server.accept()
        print("client from {address} established".format(address = address))
        connectedsocket.send(bytes(json.dumps({"response": "response here!!"}), "utf-8"))


run()