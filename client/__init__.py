import socket
import json


def create_client():
    """Função para criar uma instância de um cliente
    
    Caso de uso:
        client = create_client()
        
        # ..."""

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # criando socket IPv4 (AF_INET) com protocolo TCP (SOCK_STREAM)

    return connection