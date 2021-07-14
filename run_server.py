from server import create_server
from threading import Thread
from tests import active_threads_test


def listen_client(addr, connected_clients):
    """Função para escutar as mensagens enviadas pelos clientes.
    
    Ao receber um dicionário com todos os clientes conectados e o endereço
    correspondente ao cliente que será escutado, ficará escutando por 
    mensagens desse cliente e ao receber enviará a todos os outros."""

    ip_port = f"{addr[0]}:{addr[1]}"
    client = connected_clients[ip_port]

    while True:
        msg = client.recv(4096).decode("utf-8")

        if msg == "\quit": # Em caso da mensagem ser de desconexão do cliente
            connected_clients.pop(ip_port) # Retirando cliente da lista dos clientes conectados
            return

        for connection in connected_clients.items(): # Visitando cada cliente conectado para enviar a mensagem recebida
            if connection[0] != ip_port: # Caso o cliente seja quem enviou a mensagem, ele não a receberá, para não gerar duplicação
                connection[1].send(bytes(msg, "utf-8"))

def run():
    """Função para instanciar servidor e ficar escutando requisição do cliente"""

    server = create_server()
    connected_clients = {} # Inicializando lista de clientes conectados (como dict para acessar os índices como ip e porta do cliente em uma string, por exemplo: connected_clients["127.0.0.1:5000"])

    '''test = Thread(
            target=active_threads_test, 
            daemon = True
        )
    test.start()'''
    
    try:
        while True:
            connected_socket, address = server.accept() # Aceitando conexão do cliente

            connected_clients[f"{address[0]}:{address[1]}"] = connected_socket # Adicionando à lista com todos os clientes conectados
            print(f"client from {address[0]}:{address[1]} established")

            t = Thread(
                target=listen_client, 
                args=(address, connected_clients,), 
                daemon=True
            )
            t.start() # Iniciando uma thread para ficar escutando as mensagens enviadas por esse novo cliente

    except KeyboardInterrupt: # Em caso de derrubar o servidor com Ctrl+C
        for client in list(connected_clients.values()):
            client.shutdown()
            client.close()
        print('\n\nShutting down..')
        exit()


run()