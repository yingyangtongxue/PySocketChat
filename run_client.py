from client import create_client
import socket
import json


def run():
    """Função para instanciar cliente e conectar com servidor"""

    client = create_client()

    with open('server/configs.json') as json_file:
        configs = json.load(json_file)
        json_file.close()

    client.connect((socket.gethostname(), configs["port"]))

    while True:
        message = client.recv(1024)
        print(message.decode("utf-8"))


run()