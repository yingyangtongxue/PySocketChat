from server import create_server
from threading import Thread
import json


def listen_client(addr, connected_clients):
    """Função para escutar as mensagens enviadas pelos clientes.
    Ela rodará dentro de uma thread para cada cliente novo que se conectar."""

    ip_port = f"{addr[0]}:{addr[1]}"
    client = connected_clients[ip_port]

    while True:
        msg = client.recv(4096).decode("utf-8")

        if msg == "\quit":
            connected_clients.pop(ip_port)
            return

        for connection in connected_clients.items():
            if connection[0] != ip_port:
                connection[1].send(bytes(msg, "utf-8"))


def run():
    """Função para instanciar servidor e ficar escutando requisição do cliente"""

    server = create_server()
    connected_clients = {}

    try:
        while True:
            connected_socket, address = server.accept()

            connected_clients[f"{address[0]}:{address[1]}"] = connected_socket
            print(f"client from {address[0]}:{address[1]} established")

            t = Thread(
                target=listen_client, 
                args=(address, connected_clients,), 
                daemon=True
            )
            t.start()

    except KeyboardInterrupt:
        for client in list(connected_clients.values()):
            client.close()
        print('\n\nShutting down..')
        exit()


run()