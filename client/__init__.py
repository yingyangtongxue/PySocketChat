import socket
import json


def create_client():
    """Função para criar instância de um cliente"""

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    return connection