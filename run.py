from typing import Tuple
import client
from server import create_server
from client import create_client


def run_client():
    client = create_client()

    while True:
        message = client.recv(1024)

def run_server():
    server = create_server()

    while True:
        connectedsocket, address = server.accept()
        print("server from {address} established".format(address = address))