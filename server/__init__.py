import socket
import json


def create_server():
    """Função para criar uma instância de um servidor
    configurando qual porta será utilizada e que
    estará escutando por conexões
    
    Caso de uso:
        server = create_server()
        
        # ..."""

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # criando socket IPv4 (AF_INET) com protocolo TCP (SOCK_STREAM)

    with open('server/configs.json') as json_file:
        configs = json.load(json_file)
        json_file.close()

    connection.bind((socket.gethostname(), configs["port"])) # Atrelando o servidor ao localhost e à porta definida do json de configurações

    connection.listen()

    return connection