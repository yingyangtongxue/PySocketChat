from threading import Thread
from client import create_client
import socket
import json


def listen_messages(client):
    while True:
        msg = client.recv(4096)
        print(msg.decode())


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

        t = Thread(target = listen_messages, args = (client,))
        t.daemon = True
        t.start()

        while True:
            to_send = input(f'{username}> ')
            

    except KeyboardInterrupt:
        print('\n\nSee ya..')  
        exit()
    

run()