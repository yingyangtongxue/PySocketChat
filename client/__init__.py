import socket
import json


def create_client():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    return connection