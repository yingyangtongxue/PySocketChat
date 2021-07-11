import socket
import json


def create_client():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with open('configs.json') as json_file:
        configs = json.load(json_file)

    connection.bind((socket.gethostname(), configs["port"]))

    connection.listen(5)

    return connection