from client import create_client
import socket
import json


def run():
    """Função para instanciar cliente e conectar com servidor"""

    client = create_client()

    with open('server/configs.json') as json_file:
        configs = json.load(json_file)
        json_file.close()

    server_addr = (socket.gethostname(), configs["port"])
    client.connect(server_addr)

    try:
        username = input('Your name? ')

        while True:
            to_send = input(f'{username}> ')

    except KeyboardInterrupt:
        print('\n\nSee ya..')
        exit()


run()