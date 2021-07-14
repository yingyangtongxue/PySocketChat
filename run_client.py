from threading import Thread
from client import create_client
import socket
import json
import sys
import os

def active_windows_special_char():
    """Função para ativar os caracteres de escape ANSI no Windows. 
    Não há necessidade no Linux"""
    if os.name == 'nt':
        from ctypes import windll
        k = windll.kernel32
        k.SetConsoleMode(k.GetStdHandle(-11), 7)

def listen_messages(client, display):
    while True:
        msg = client.recv(4096).decode("utf-8") # recebe a mensagem do servidor
        sys.stdout.write('\x1b[0G')             # move o cursor do terminal para o inicio da linha
        sys.stdout.write('\x1b[0K')             # apaga toda a linha a partir do cursor até o fim
        print(msg)                              # imprime a mensagem do servidor
        print(display, end="", flush=True)      # imprime o display para inserção de nova mensagem

def run():
    """Função para instanciar cliente e conectar com servidor"""

    client = create_client()

    with open('server/configs.json') as json_file: # Abre o JSON com as configurações que serão usadas
        configs = json.load(json_file)
        json_file.close()

    server_addr = (socket.gethostname(), configs["port"])
    client.connect(server_addr)

    try:
        active_windows_special_char()           # Faz tratamento de caracteres especiais
        username = input('Your name? ')
        display = f'{username}> '

        t = Thread(
            target = listen_messages, 
            args = (client, display,)
        )
        t.daemon = True
        t.start()                               # Inicia uma thread para ficar escutando mensagens que chegam do servidor

        print("welcome to the chat\n\n")
        while True:
            to_send = input(display)
            client.sendto(bytes(display+to_send, "utf-8"), (socket.gethostname(), configs["port"])) # Envia a mensagem digitada pelo cliente atual para o servidor

    except KeyboardInterrupt: # Em caso de derrubar o servidor com Ctrl+C
        client.sendto(bytes("\\quit", "utf-8"), (socket.gethostname(), configs["port"])) # Mandando mensagem ao servidor para desconexão
        client.close()
        print('\n\nSee ya..')  
        exit()


run()