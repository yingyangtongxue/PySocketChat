import socket
import json


def create_server():
    """Função para criar uma instância de um servidor"""

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with open('server/configs.json') as json_file:
        configs = json.load(json_file)
        json_file.close()

    connection.bind((socket.gethostname(), configs["port"]))

    connection.listen()

    return connection