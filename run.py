from server import create_server
from client import create_client
from threading import Thread
import socket
import json


def run_client():
    """Função para instanciar cliente e conectar com servidor"""

    client = create_client()

    with open('server/configs.json') as json_file:
        configs = json.load(json_file)
        json_file.close()

    client.connect((socket.gethostname(), configs["port"]))

    while True:
        message = client.recv(1024)
        print(message.decode("utf-8"))

def run_server():
    """Função para instanciar servidor e ficar escutando requisição do cliente"""

    server = create_server()

    while True:
        connectedsocket, address = server.accept()
        print("server from {address} established".format(address = address))
        connectedsocket.send(bytes(json.dumps({"response": "response here!!"}), "utf-8"))

def run():
    server_thread = Thread(target=run_server)
    client_thread = Thread(target=run_client)

    server_thread.start()
    client_thread.start()

run()